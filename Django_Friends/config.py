# -*- coding: utf-8 -*-
# @Time    : 19-2-13 下午7:43
# @Author  : SamSa
# @Email   : sajinde@qq.com
# @File    : config.py
# @statement:项目以及第三方配置

# 云之讯短信平台配置
YZX_SMS_API = 'https://open.ucpaas.com/ol/sms/sendsms'
YZX_SMS_PARAMS = {
    "sid": 'a9f0c6e073539cb1946b0ff901816aed',
    "token": 'e5831a53e875a8fb73371caa146ed182',
    "appid": '33eb8c92d2e4471e9d64c77e99a7201a',
    "templateid": "430588",
    "param": None,
    "mobile": None,
}


# 七牛云配置
QN_ACCESS_KEY = 'j4mpIn_WwSnM8EfYGGXqmq33b-GsYqdGflLOBKRL'
QN_SECRET_KEY = 'fUzrs4GqcU1DVgE3mLCA8RuE4Z5Gyv5tVFcnSqfF'
QN_HOST = 'http://pmy2ozqbl.bkt.clouddn.com'
QN_BUCKET = 'tantan'

# 反悔次数

BACK_TIME = 3

# 滑动积分
SWIPE_SCORE = {
    'like': 5,
    'superlike': 7,
    'dislike': -5,
}

