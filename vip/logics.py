# -*- coding: utf-8 -*-
# @Time    : 19-2-18 下午7:05
# @Author  : SamSa
# @Email   : sajinde@qq.com
# @File    : logics.py
# @statement:
from common import errors


def perm_check(perm_name):
    """权限控制装饰器"""
    def check(view_func):
        def wrapper(request):
            if request.user.vip.has_perm(perm_name):
                return view_func(request)
            else:
                raise errors.PermError
        return wrapper
    return check