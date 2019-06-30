from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Server(models.Model):
    """服务器设备"""

    # sub_asset_type_choice = (
    #     (0, '阿里云'),
    #     (1, '用友云'),
    # )
    #
    # sub_BusinessUnit_choice = (
    #     (0, '友报账'),
    #     (1, '友帐表'),
    #     (2, '友报表'),
    #     (3, '电子档案'),
    # )

    # sub_asset_type = models.SmallIntegerField(choices=sub_asset_type_choice, default=0, verbose_name="服务器类型")
    # sub_BusinessUnit_type = models.SmallIntegerField(choices=sub_BusinessUnit_choice, default=0, verbose_name="产品线")
    hostname = models.CharField(max_length=128, null=True, blank=True, verbose_name='主机名')
    ip_addr = models.GenericIPAddressField('IP_addr', blank=True, null=True)
    # cpu = models.IntegerField(default=1, verbose_name="cpu")
    # mem = models.IntegerField(default=1, verbose_name="mem")
    # sys_disk = models.IntegerField(default=1, verbose_name="sys_disk")
    # data_disk = models.IntegerField(default=1, verbose_name="data_disk")
    # account = models.CharField(max_length=64, null=True, blank=True, verbose_name='account')
    # password = models.CharField(max_length=64, null=True, blank=True, verbose_name='password')



    def __str__(self):
        # return '%s-%s-%s' % (self.get_sub_asset_type_display(), self.get_sub_BusinessUnit_type_display(), self.ip_addr)
        return '%s-%s' % (self.hostname, self.ip_addr)

    class Meta:
        verbose_name = '服务器'
        verbose_name_plural = "服务器"
