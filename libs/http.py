# -*- coding: utf-8 -*-
# @Time    : 19-2-13 下午7:59
# @Author  : SamSa
# @Email   : sajinde@qq.com
# @File    : http.py
# @statement: 封装返回json数据

import json

from django.http import HttpResponse
from Django_Friends import settings


def render_json(data=None, code=0):
    result = {
        'data': data,
        'code': code
    }

    if settings.DEBUG:
        json_str = json.dumps(result, ensure_ascii=False, indent=4, sort_keys=True)
    else:
        json_str = json.dumps(result, ensure_ascii=False, separators=(',', ':'))

    return HttpResponse(json_str)
