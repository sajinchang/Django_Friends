from django.db import models

# Create your models here.
from django.db.models import Q

from Django_Friends import config
from common import keys
from libs.cache import cache_redis
from common import errors


class Swiped(models.Model):
    """滑动用户"""
    FLAGS = (
        ('like', '喜欢'),
        ('superlike', '超级喜欢'),
        ('dislike', '不喜欢'),
    )
    uid = models.IntegerField(verbose_name='滑动者的 uid')
    sid = models.IntegerField(verbose_name='被滑动者的 uid')
    flag = models.CharField(max_length=16, choices=FLAGS, verbose_name='滑动类型')
    time = models.DateTimeField(auto_now_add=True, verbose_name='滑动时间')

    @classmethod
    def is_like(cls, uid, sid):
        """检查是否喜欢过某人"""
        return cls.objects.filter(uid=uid, sid=sid,
                                  flag__in=['like', 'superlike']).exists()

    @classmethod
    def swiped(cls, uid, sid, flag):
        """记录滑动,不可以重复滑动某个人"""
        flags = [_flag[0] for _flag in cls.FLAGS]
        if flag not in flags:
            raise errors.FlagError
        cls.objects.update_or_create(uid=uid, sid=sid,
                                     defaults={
                                         'flag': flag
                                     })

        # 滑动积分存入redis  使用有序集合
        score = config.SWIPE_SCORE.get(flag, 0)
        cache_redis.zincrby(keys.HOTRANK, sid, score)


    @classmethod
    def show_like_me(cls,uid):
        """查看喜欢我的id列表"""
        swipeds_id = cls.objects.filter(sid=uid,flag__in=['like', 'superlike']).only('uid')
        return [swiped_id.uid for swiped_id in swipeds_id]

    class Meta:
        db_table = 'swiped'


class Friend(models.Model):
    """好友模型"""
    uid1 = models.IntegerField()
    uid2 = models.IntegerField()

    @classmethod
    def make_friend(cls, uid1, uid2):
        """建立好友关系   因为多出使用,所以使用类方法放在模型中"""
        uid1, uid2 = (uid1, uid2) if int(uid1) < int(uid2) else (uid2, uid1)
        cls.get_or_create(uid1=uid1, uid2=uid2)

    @classmethod
    def break_friend(cls, uid1, uid2):
        """撤销好友关系"""
        uid1, uid2 = (uid1, uid2) if uid1 < uid2 else (uid2, uid1)
        # filter比get更加安全
        cls.objects.filter(uid1=uid1, uid2=uid2).delete()

    @classmethod
    def show_friends(cls, uid):
        """获取好友的id"""
        friends_id = []
        relationship = Q(uid1=uid) | Q(uid2=uid)
        for friend in cls.objects.filter(relationship):
            friend_id = friend.uid1 if uid == friend.uid2 else friend.uid2
            friends_id.append(friend_id)

        return friends_id

    class Meta:
        db_table = 'friends'
