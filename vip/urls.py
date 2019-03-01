# -*- coding: utf-8 -*-
# @Time    : 19-2-18 上午11:45
# @Author  : SamSa
# @Email   : sajinde@qq.com
# @File    : urls.py
# @statement:
from django.conf.urls import url

from vip import views


urlpatterns = [
    url(r'^show_vip/', views.show_vip, name='show_vip')
]