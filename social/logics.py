# -*- coding: utf-8 -*-
# @Time    : 19-2-15 上午11:54
# @Author  : SamSa
# @Email   : sajinde@qq.com
# @File    : logics.py
# @statement:
import datetime
import time

from django.core.cache import cache
from Django_Friends import config

from common import errors, keys
from social.models import Swiped, Friend
from user.models import User

from libs.cache import cache_redis



def rcmd_list(user):
    """获取推荐列表"""

    # 获取最大年龄以及最小年龄
    today = datetime.datetime.today()
    max_age = today.year - user.profile.min_dating_age
    min_age = today.year - user.profile.max_dating_age

    # 选出已经被划过的user
    swipeds = Swiped.objects.filter(uid=user.id).only('sid')
    swiped_ids = [swiped.sid for swiped in swipeds]

    # 满足要求的user
    users = User.objects.filter(
        sex = user.profile.dating_sex,
        birth_year__gte=min_age,
        birth_year__lte=max_age,
        location=user.profile.location).exclude(id__in=swiped_ids)[:15]
    return users


def like_someone(uid, sid):
    """喜欢某人  逻辑实现"""
    # 添加滑动记录
    Swiped.swiped(uid, sid, flag='like')

    # 检查对方是否喜欢过你,如果是则建立好友关系
    if Swiped.is_like(sid, uid):
        Friend.make_friend(uid, sid)
        return True
    return False


def super_like_someone(uid, sid):
    """超级喜欢某人  逻辑实现"""
    # 添加滑动记录
    Swiped.swiped(uid, sid, flag='superlike')

    # 检查对方是否喜欢过你,如果是则建立好友关系
    if Swiped.is_like(sid, uid):
        Friend.make_friend(uid, sid)
        return True
    return False


def go_back(uid):
    """反悔操作逻辑实现  每天每个用户可以反悔3次"""
    key = keys.BACK_TIME % uid
    back_time = cache.get(key, 0)
    if back_time >= config.BACK_TIME:
        raise errors.BackLimitError

    timeout = 86400 - (time.time() + 8 * 3600) % 86400
    cache.set(key, back_time + 1, timeout)

    # 根据时间字段查找出最近添加的滑动
    try:
        swiped = Swiped.objects.filter(uid=uid).latest('time')

        # 反悔操作对积分进行恢复
        score = config.SWIPE_SCORE.get(swiped.flag, 0)
        cache_redis.zincrby(keys.HOTRANK, swiped.sid, -score)

    except Swiped.DoesNotExist:
        return None

    # 已经建立好友关系则撤销
    if swiped.flag in ['like', 'superlike']:
        Friend.break_friend(uid1=uid, uid2=swiped.sid)
    swiped.delete()



def get_top_num(num):
    """获取积分最高的前num个用户"""

    # withscores=True   表示以成绩进行升序
    top_data = cache_redis.zrevrange(keys.HOTRANK, 0, num - 1, withscores=True)
    clean_data = [[int(uid), int(score)] for uid, score in top_data]

    user_id_list = [uid for uid, _ in clean_data]
    user_info_list = User.objects.filter(id__in=user_id_list)
    users = sorted(user_info_list, key=lambda user: user_id_list.index(user.id))
    data = []
    for user, (_, score)in zip(users,clean_data):
        data.append([user, score])

    return data
