# -*- coding: utf-8 -*-
# @Time    : 19-2-14 下午6:23
# @Author  : SamSa
# @Email   : sajinde@qq.com
# @File    : form.py
# @statement:表单信息验证
from django import forms

from user.models import Profile


class FormProfile(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [
            'dating_sex', 'location',
            'min_distance', 'max_distance',
            'min_dating_age', 'max_dating_age',
            'vibration', 'only_matche', 'auto_play',
        ]

    def clean_max_dating_age(self):
        """
        验证某个字段必须是 clean_xxx 的形式，
        并且验证出现问题，需要手动抛出异常，若没有问题则返回验证的字段
        """
        cleaned_data = super().clean()
        min_dating_age = cleaned_data['min_dating_age']
        max_dating_age = cleaned_data['max_dating_age']

        if min_dating_age > max_dating_age:
            # 手动抛出异常
            raise forms.ValidationError('最小年龄必须小于最大年龄')
        else:
            # 如果没有问题，与要将验证后的数据返回
            return max_dating_age

    def clean_max_distance(self):
        cleaned_data = super().clean()
        min_distance = cleaned_data['min_distance']
        max_distance = cleaned_data['max_distance']

        if min_distance > max_distance:
            raise forms.ValidationError('最小距离必须大于最大距离')
        else:
            return max_distance

