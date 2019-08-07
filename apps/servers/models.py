from datetime import datetime

from django.db import models

from users.models import UserProfile


# 定义资产model
class Server(models.Model):
    zctype = models.ForeignKey('servers.ServerType', on_delete=models.CASCADE)
    ipaddress = models.CharField(max_length=100, verbose_name='IP地址', blank=True)
    description = models.CharField(max_length=50, verbose_name='功能描述', blank=True)
    brand = models.CharField(max_length=50, verbose_name='设备品牌', blank=True)
    zcmodel = models.CharField(max_length=50, verbose_name='设备型号', blank=True)
    zcnumber = models.CharField(max_length=50, verbose_name='设备序号', blank=True)
    zcpz = models.CharField(max_length=100, verbose_name='设备配置', blank=True)
    owner = models.ForeignKey('users.UserProfile', on_delete=models.SET_NULL, null=True, blank=True)
    undernet = models.CharField(max_length=10, verbose_name='所在网络')
    guartime = models.CharField(max_length=50, verbose_name='保修期', blank=True)
    comment = models.CharField(max_length=300, verbose_name='备注', blank=True)
    modify_time = models.DateTimeField(default=datetime.now, verbose_name='修改时间')

    class Meta:
        verbose_name = '资产表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.undernet


# 定义资产类型model
class ServerType(models.Model):
    zctype = models.CharField(max_length=20, verbose_name='资产类型')

    class Meta:
        verbose_name = '资产类型表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zctype


# 定义资产历史model
class ServerHis(models.Model):
    serverid = models.IntegerField(verbose_name='资产ID')
    zctype = models.CharField(max_length=20, verbose_name='资产类型')
    ipaddress = models.CharField(max_length=100, verbose_name='IP地址', blank=True)
    description = models.CharField(max_length=50, verbose_name='功能描述', blank=True)
    brand = models.CharField(max_length=50, verbose_name='设备品牌', blank=True)
    zcmodel = models.CharField(max_length=50, verbose_name='设备型号', blank=True)
    zcnumber = models.CharField(max_length=50, verbose_name='设备序号', blank=True)
    zcpz = models.CharField(max_length=100, verbose_name='设备配置', blank=True)
    owner = models.CharField(max_length=20, verbose_name='管理人员')
    undernet = models.CharField(max_length=10, verbose_name='所在网络')
    guartime = models.CharField(max_length=50, verbose_name='保修期', blank=True)
    comment = models.CharField(max_length=300, verbose_name='备注', blank=True)
    modify_time = models.DateTimeField(default=datetime.now, verbose_name='修改时间')

    class Meta:
        verbose_name = '资产历史表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.zctype
