# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from libs.http import render_json
from social import logics
from social.models import Swiped, Friend
from user.models import User
from vip.logics import perm_check


def rcmd(request):
    """推荐列表"""
    users = logics.rcmd_list(request.user)
    user_info = [user.to_dict() for user in users]
    return render_json(data=user_info)


@csrf_exempt
def like(request):
    """滑动 喜欢"""
    sid = request.POST.get('sid')
    match = logics.like_someone(request.user.id, sid)
    return render_json(data=match)


@csrf_exempt
@perm_check('superlike')
def super_like(request):
    """滑动  超级喜欢"""
    sid = request.POST.get('sid')
    match = logics.super_like_someone(request.user.id, sid)
    return render_json(data=match)


@csrf_exempt
def dislike(request):
    """不喜欢"""
    sid = request.POST.get('sid')
    # 直接添加滑动记录
    Swiped.swiped(uid=request.user.id, sid=sid, flag='dislike')
    return render_json()


@perm_check('back')
def back(request):
    """反悔操作 """
    logics.go_back(request.user.id)
    return render_json()


@perm_check('like_me')
def like_me(request):
    """查看喜欢我的人"""
    uid_list = Swiped.show_like_me(request.user.id)
    users = User.objects.filter(id__in=uid_list)
    users_info = [user.to_dict() for user in users]
    return render_json(data=users_info)


def friends(request):
    """展示好友列表"""
    friends_id = Friend.show_friends(request.user.id)
    friend_list = User.objects.filter(id__in=friends_id)
    friend_info_list = [frd.to_dict() for frd in friend_list]
    return render_json(data=friend_info_list)


def top10(request):
    """展示全服积分最高的10位用户"""
    top_info = logics.get_top_num(10)
    rst = [[user.to_dict(), score] for user, score in top_info]
    return render_json(data=rst)
