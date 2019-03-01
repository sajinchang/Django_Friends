# -*- coding: utf-8 -*-
# @Time    : 19-2-14 下午6:00
# @Author  : SamSa
# @Email   : sajinde@qq.com
# @File    : middleware.py
# @statement:判断登录状态中间件
from django.utils.deprecation import MiddlewareMixin

from common import errors
from libs.http import render_json
from user.models import User


class AuthMiddleWare(MiddlewareMixin):
    """登录状态"""
    WHITE_LIST = [

        '/user/submit_phone/',
        '/user/submit_vcode/',
        '/vip/show_vip/',

    ]

    def process_request(self,request):
        if request.path in self.WHITE_LIST:
            return None

        uid = request.session.get('uid')
        if uid:
            request.user = User.objects.get(id=uid)
        else:
            return render_json(code=errors.LoginError.code)


class ErrorMiddleWare(MiddlewareMixin):
    """error code"""
    def process_exception(self, request, exception):
        """错误码处理"""
        if isinstance(exception, errors.Error):
            return render_json(code=exception.code)
