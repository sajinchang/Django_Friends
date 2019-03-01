# -*- coding: utf-8 -*-
# @Time    : 19-2-13 下午7:19
# @Author  : SamSa
# @Email   : sajinde@qq.com
# @File    : urls.py
# @statement:
from django.conf.urls import url

from user import views

urlpatterns = [
    url(r'^submit_phone/', views.submit_phone, name='submit_phone'),
    url(r'^submit_vcode/', views.submit_vcode, name='submit_vcode'),
    url(r'^get_profile/', views.get_profile, name='get_file'),
    url(r'^set_profile/', views.set_profile, name='set_profile'),
    url(r'^upload_avatar/', views.upload_avatar, name='upload_avatar'),
]