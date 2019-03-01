# -*- coding: utf-8 -*-
# @Time    : 19-2-21 下午5:18
# @Author  : SamSa
# @Email   : sajinde@qq.com
# @File    : cache.py
# @statement:

from redis import Redis
from django.conf import settings

cache_redis = Redis(**settings.REDIS)     # `**` 将字典拆开一一传入函数行参的对应位置, 一个 `*` 类似于指针
