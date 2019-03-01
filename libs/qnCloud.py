# -*- coding: utf-8 -*-
# @Time    : 19-2-14 下午8:16
# @Author  : SamSa
# @Email   : sajinde@qq.com
# @File    : qnCloud.py
# @statement:保存到七牛云
from qiniu import Auth, put_file

from Django_Friends import config


def upload_qnCloud(filename, filepath):
    """文件上传至七牛云"""

    # 构建建权对象
    qn_auth = Auth(access_key=config.QN_ACCESS_KEY, secret_key=config.QN_SECRET_KEY)

    # 生成上传token   指定过期时间
    token = qn_auth.upload_token(config.QN_BUCKET, filename, 3600)

    # upload
    ret, info = put_file(token, filename, filepath)
    return ret, info
