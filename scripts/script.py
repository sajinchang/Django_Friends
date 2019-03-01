    # -*- coding: utf-8 -*-
# @Time    : 19-2-15 下午5:52
# @Author  : SamSa
# @Email   : sajinde@qq.com
# @File    : script.py
# @statement:
import os
import random
import sys

import django


# 设置环境

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django_TanTan.settings")
django.setup()


from user.models import User

from vip.models import Vip, Permission, VipPerm


last_names = (
    '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨'
    '朱秦尤许何吕施张孔曹严华金魏陶姜'
    '戚谢邹喻柏水窦章云苏潘葛奚范彭郎'
    '鲁韦昌马苗凤花方俞任袁柳酆鲍史唐'
    '费廉岑薛雷贺倪汤滕殷罗毕郝邬安常'
    '乐于时傅皮卞齐康伍余元卜顾孟平黄'
)

first_names = {
    'male': [
        '致远', '俊驰', '雨泽', '烨磊', '晟睿',
        '天佑', '文昊', '修洁', '黎昕', '远航',
        '旭尧', '鸿涛', '伟祺', '荣轩', '越泽',
        '浩宇', '瑾瑜', '皓轩', '浦泽', '绍辉',
        '绍祺', '升荣', '圣杰', '晟睿', '思聪'
    ],
    'female': [
        '沛玲', '欣妍', '佳琦', '雅芙', '雨婷',
        '韵寒', '莉姿', '雨婷', '宁馨', '妙菱',
        '心琪', '雯媛', '诗婧', '露洁', '静琪',
        '雅琳', '灵韵', '清菡', '溶月', '素菲',
        '雨嘉', '雅静', '梦洁', '梦璐', '惠茜'
    ]
}


def random_name():
    """随机生成姓名"""
    last_name = random.choice(last_names)
    sex = random.choice(list(first_names.keys()))
    first_name = random.choice(first_names[sex])

    return ''.join([last_name, first_name]), sex


def create_robots(num):
    """创建机器人用户"""
    for i in range(num):
        name, sex = random_name()
        try:
            User.objects.create(
                sex=sex,
                nickname=name,
                location=random.choice(['bj', 'sh', 'gz', 'sz', 'cd', 'xa', 'wh']),
                birth_year=random.randint(1980,2000),
                birth_month=random.randint(1,12),
                birth_day=random.randint(1,28),
                phonenum=random.randint(21000000000,29000000000))
            print('robot:%s\t%s'%(name,sex))
        except Exception as e:
            print(e)



def init_perm():
    """创建权限数据"""
    permission = (
        ('vipflag', '会员身份标识'),
        ('superlike', '超级喜欢'),
        ('back', '反悔功能'),
        ('anylocation', '任意更改定位'),
        ('unlimit_like', '无限喜欢次数'),
        ('like_me', '查看喜欢过我的人'),
    )

    for name, desc in permission:
        perm, _ = Permission.objects.get_or_create(name=name, desc=desc)

        print(perm)


def init_vip():
    """创建vip数据"""
    for i in range(4):
        name = '%s级会员' % i
        price = 5 * i
        vip, _ = Vip.objects.get_or_create(name=name, level=i, price=price)
        print(vip.name)


def create_vip_perm():
    """创建会员权限关系表"""

    # 获取vip
    vip1 = Vip.objects.get(level=1)
    vip2 = Vip.objects.get(level=2)
    vip3 = Vip.objects.get(level=3)

    # 获取权限
    vipflag = Permission.objects.get(name='vipflag')
    superlike = Permission.objects.get(name='superlike')
    back = Permission.objects.get(name='back')
    anylocation = Permission.objects.get(name='anylocation')
    unlimit_like = Permission.objects.get(name='unlimit_like')
    like_me = Permission.objects.get(name='like_me')

    # vip1权限
    VipPerm.objects.get_or_create(vip_id=vip1.id, perm_id=vipflag.id)
    VipPerm.objects.get_or_create(vip_id=vip1.id, perm_id=superlike.id)

    # 给 VIP 2 分配权限
    VipPerm.objects.get_or_create(vip_id=vip2.id, perm_id=vipflag.id)
    VipPerm.objects.get_or_create(vip_id=vip2.id, perm_id=superlike.id)
    VipPerm.objects.get_or_create(vip_id=vip2.id, perm_id=back.id)

    # 给 VIP 3 分配权限
    VipPerm.objects.get_or_create(vip_id=vip3.id, perm_id=vipflag.id)
    VipPerm.objects.get_or_create(vip_id=vip3.id, perm_id=superlike.id)
    VipPerm.objects.get_or_create(vip_id=vip3.id, perm_id=back.id)
    VipPerm.objects.get_or_create(vip_id=vip3.id, perm_id=anylocation.id)
    VipPerm.objects.get_or_create(vip_id=vip3.id, perm_id=unlimit_like.id)
    VipPerm.objects.get_or_create(vip_id=vip3.id, perm_id=like_me.id)


if __name__ == '__main__':
    # create_robots(5000)
    # init_vip()
    # init_perm()
    # create_vip_perm()
    pass

