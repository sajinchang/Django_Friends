from django.core.cache import cache
import logging

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from user.logics import is_phone_num, send_Vcode, save_upload_file
from libs.http import render_json
from common import errors, keys
from user.form import FormProfile
from user.models import User


info_log = logging.getLogger('inf')


@csrf_exempt
def submit_phone(request):
    """发送验证码"""

    phone_num = request.POST.get('phonenum')
    if is_phone_num(phone_num):
        if send_Vcode(phone_num=phone_num):
            return render_json(data={
                'msg': 'OK',
            })


        return render_json(code=errors.PlatformError.code)
    return render_json(code=errors.PhoneError.code)


@csrf_exempt
def submit_vcode(request):
    """提交验证码进行注册登录"""
    phone_num = request.POST.get('phonenum')

    vcode = request.POST.get('vcode')
    if vcode == cache.get(keys.VCode % phone_num):
        user, _ = User.get_or_create(phonenum=phone_num, nickname=phone_num)
        # 记录登录状态
        request.session['uid'] = user.id
        # 记录登录日志
        info_log.info(f'uid = {user.id}')
        return render_json(data=user.to_dict())

    return render_json(code=errors.VcodeError.code)


def get_profile(request):
    """获取个人资料,首先判断登录状态"""
    profile_date = request.user.to_dict('vibration', 'only_matche', 'auto_play')
    return render_json(data=profile_date)


@csrf_exempt
def set_profile(request):
    """修改个人资料"""
    # 表单验证
    form_data = FormProfile(request.POST)
    # 如果验证没有问题

    if form_data.is_valid():
        # 只保存，不提交
        profile = form_data.save(commit=False)
        profile.id = request.user.id
        profile.save()
        return render_json()

    return render_json(data=form_data.errors, code=errors.ProfileError.code)


@csrf_exempt
def upload_avatar(request):
    """上传用户头像"""
    avatar = request.FILES.get('avatar')
    save_upload_file.delay(request.user, avatar)
    return render_json()
