# -*- coding: utf-8 -*-
# @Time    : 19-2-21 上午11:51
# @Author  : SamSa
# @Email   : sajinde@qq.com
# @File    : gunicorn_config.py
# @statement:gunicorn配置项

from multiprocessing import cpu_count

"""
初始化数据库,注意初始化位置,在项目加载之前初始化,
否则抛出异常:         raise HaltServer(reason, self.WORKER_BOOT_ERROR)
                gunicorn.errors.HaltServer: <HaltServer 'Worker failed to boot.' 3>
"""
# import pymysql
#
# pymysql.install_as_MySQLdb()


bind = ['127.0.0.1:9000']           # 线上环境不会开启在公网 IP 下，一般使用内网 IP
daemon = True                       # 是否开启守护进程模式
# daemon = False                    # 是否开启守护进程模式
pidfile = 'logs/gunicorn.pid'

workers = cpu_count() * 2           # 工作进程数量
worker_class = 'gevent'             # 指定一个异步处理的库
worker_connections = 65535

keepalive = 60                      # 服务器保持链接时间,避免频繁的tcp连接
timeout = 30
graceful_timeout = 10
forwarded_allow_ips = '*'

# 日志处理
capture_output = True
loglevel = 'info'
errorlog = 'logs/gunicorn_error.log'




