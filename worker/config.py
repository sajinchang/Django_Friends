# -*- coding: utf-8 -*-
# @Time    : 19-2-14 下午9:03
# @Author  : SamSa
# @Email   : sajinde@qq.com
# @File    : config.py
# @statement:

broker_url = 'redis://127.0.0.1:6379/7'
broker_pool_limit = 100  # Borker 连接池, 默认是10

timezone = 'Asia/Shanghai'
accept_content = ['pickle', 'json']

task_serializer = 'pickle'

result_backend = 'redis://127.0.0.1:6379/7'
result_serializer = 'pickle'
result_cache_max = 1000  # 任务结果最大缓存数量
result_expires = 3600  # 任务过期时间

worker_redirect_stdouts_level = 'INFO'
