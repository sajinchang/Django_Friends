# -*- coding: utf-8 -*-
# @Time    : 19-2-14 下午10:14
# @Author  : SamSa
# @Email   : sajinde@qq.com
# @File    : urls.py
# @statement:
from django.conf.urls import url

from social import views

urlpatterns = [
    url(r'^rcmd/', views.rcmd, name='rcmd'),
    url(r'^like/', views.like, name='like'),
    url(r'^super/', views.super_like, name='super'),
    url(r'^dislike/', views.dislike, name='dislike'),
    url(r'^back/', views.back, name='back'),
    url(r'^likeme/', views.like_me, name='likeme'),
    url(r'^friends/', views.friends, name='friends'),
    url(r'^top10/', views.top10)

]