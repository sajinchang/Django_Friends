from django.db import models


class Vip(models.Model):
    """Vip模型"""
    name = models.CharField(max_length=16, unique=True, verbose_name='会员名称')
    price = models.FloatField(default=0, verbose_name='会员价格')
    level = models.IntegerField(unique=True, verbose_name='会员等级')

    class Meta:
        db_table = 'vip'

    def perms(self):
        """查出每种vip的所有权限"""
        relation_list = VipPerm.objects.filter(vip_id=self.id).only('perm_id')
        perm_id_list = [real.perm_id for real in relation_list ]

        perm_list = Permission.objects.filter(pk__in=perm_id_list).only('name')
        return [perm.name for perm in perm_list]

    def has_perm(self, perm_name):
        """检查vip是否拥有某权限"""
        permission_names = self.perms()
        if perm_name in permission_names:
            return True
        return False


class Permission(models.Model):
    """权限模型"""
    desc = models.TextField(verbose_name='权限描述')
    name = models.CharField(max_length=16, unique=True, verbose_name='名称')

    class Meta:
        db_table = 'permission'


class VipPerm(models.Model):
    """会员权限关系表"""
    vip_id = models.IntegerField(verbose_name='会员id')
    perm_id = models.IntegerField(verbose_name='权限id')

    class Meta:
        db_table = 'vip_perm'
