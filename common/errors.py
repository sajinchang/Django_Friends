# -*- coding: utf-8 -*-
# @Time    : 19-2-13 下午8:16
# @Author  : SamSa
# @Email   : sajinde@qq.com
# @File    : errors.py
# @statement:错误码


class Error(Exception):
    """错误基类"""
    pass


def create_error(name, code):
    """创建一个错误类"""
    return type(name, (Error,), {'code': code})


OK = create_error('OK', 0)
PlatformError = create_error('PLATFORM_ERR', 1000)      # 第三方平台错误
PhoneError = create_error('PHONE_ERR', 1001)            # 手机号错误
VcodeError = create_error('VCODE_ERR', 1002)            # 无效的验证码
LoginError = create_error('LOGIN_REQUIRE', 1003)        # 用户未登录
ProfileError = create_error('PROFILE_ERR', 1004)        # 个人资料错误
FlagError = create_error('FLAGERR', 1005)               # 滑动类型错误
BackLimitError = create_error('BACKLIMITERR',1006)      # 反悔次数上限
PermError = create_error('PERMERROR', 1007)             # 权限不足


