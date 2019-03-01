# -*- coding: utf-8 -*-
# @Time    : 19-2-14 下午5:26
# @Author  : SamSa
# @Email   : sajinde@qq.com
# @File    : orm.py
# @statement:

from django.db import models

from django.core.cache import cache

from common import keys


def to_dict(self, *exculde):
    """以字典的形式返回数据模型"""
    attr_name = {}
    for field in self._meta.fields:
        field_name = field.attname
        if field_name not in exculde:
            attr_name[field_name] = getattr(self, field_name)
    return attr_name


def get(cls, *args, **kwargs):
    """封装Model的get函数
        加入缓存机制
    """
    pk = kwargs.get('id') or kwargs.get('pk')
    if pk:
        key = keys.MODEL % (cls.__name__, pk)
        model_obj = cache.get(key)
        if isinstance(model_obj, cls):
            return model_obj

    model_obj = cls.objects.get(*args, **kwargs)
    key = keys.MODEL % (cls.__name__, model_obj.id)
    cache.set(key, model_obj)
    return model_obj


def get_or_create(cls, default=None, **kwargs):
    """封装Model的get_or_create函数
        加入缓存机制
    """
    pk = kwargs.get('id') or kwargs.get('pk')
    if pk:
        key = keys.MODEL % (cls.__name__, pk)
        model_obj = cache.get(key)
        if isinstance(model_obj, cls):
            return model_obj, False

    model_obj, is_created = cls.objects.get_or_create(default, **kwargs)
    key = keys.MODEL % (cls.__name__, model_obj.id)
    cache.set(key, model_obj)
    return model_obj, is_created


def save(self, force_insert=False, force_update=False, using=None,
         update_fields=None):
    """重写save方法, 添加缓存机制"""
    self._save(force_insert, force_update, using, update_fields)
    key = keys.MODEL % (self.__class__.__name__, self.pk)
    cache.set(key, self)


def patch_model():
    """为model.Model打补丁, 动态添加方法  MonkeyPatch"""
    models.Model.to_dict = to_dict

    models.Model.get = classmethod(get)
    models.Model.get_or_create = classmethod(get_or_create)

    models.Model._save = models.Model.save
    models.Model.save = save