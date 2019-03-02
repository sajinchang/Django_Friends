# -*- coding: utf-8 -*-
# @Time    : 19-2-14 下午9:02
# @Author  : SamSa
# @Email   : sajinde@qq.com
# @File    : script.py.py
# @statement:

import os


from celery import Celery

from worker import config

# 设置默认django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_Friends.settings')

celery_app = Celery('Django_Friends')
celery_app.config_from_object(config)
celery_app.autodiscover_tasks()

