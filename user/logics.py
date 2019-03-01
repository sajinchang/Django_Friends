# -*- coding: utf-8 -*-
# @Time    : 19-2-13 下午8:32
# @Author  : SamSa
# @Email   : sajinde@qq.com
# @File    : logics.py
# @statement:发送短信验证码
import os
import re
from random import randrange
from urllib.parse import urljoin

import requests

from django.core.cache import cache

from common import keys
from Django_Friends import config
from django.conf import settings

from libs.qnCloud import upload_qnCloud
from worker import celery_app


def is_phone_num(phone_num):
    """验证是否为手机号"""
    pattern = '^((13[0-9])|(14[5,7])|(15[0-3,5-9])|(17[0,3,5-8])|(18[0-9])|166|198|199|(147))\\d{8}$'
    return True if re.match(pattern, str(phone_num)) else False


def V_code(length=4):
    """ 生成验证码"""
    code = randrange(10 ** length)
    template = '%%0%dd' % length
    return template % code


def send_Vcode(phone_num):
    """ 向第三方发送验证码"""
    v_code = V_code()
    print('验证码' + v_code)
    # 将验证码存入缓存中
    cache.set(keys.VCode % phone_num, v_code, 300)

    params = config.YZX_SMS_PARAMS.copy()
    params['mobile'] = phone_num
    params['param'] = v_code

    # 向第三方发送验证码
    response = requests.post(config.YZX_SMS_API, json=params)

    if response.status_code == 200:
        result = response.json()
        print(result)

        if result.get('msg') == 'OK':
            return True
    return False


def save_upload_file_local(filename, upload_file):
    """文件保存到本地"""
    filepath = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT, filename)

    with open(filepath, 'wb') as fp:
        for chunk in upload_file.chunks():
            fp.write(chunk)

    return filepath


@celery_app.task
def save_upload_file(user, avatar):
    """保存用户的头像"""
    filename = keys.VCode % user.id
    filepath = save_upload_file_local(filename,avatar)

    # 保存到七牛云
    upload_qnCloud(filename, filepath)

    # 记录图像的url
    user.avatar = urljoin(config.QN_HOST, filename)
    user.save()
