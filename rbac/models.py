from django.db import models


# Create your models here.
class User(models.Model):
    '''用户表'''
    username = models.CharField(max_length=32, verbose_name='用户名')
    password = models.CharField(max_length=64, verbose_name='密码')
    user2role = models.ManyToManyField('Role', verbose_name='所属角色',
    blank = True)

    class Meta:
        verbose_name_plural = '用户表'

    def __str__(self):
        return self.username


class Role(models.Model):
    '''角色表'''
    rolename = models.CharField(max_length=32, verbose_name='角色名')
    role2per = models.ManyToManyField('Permission', verbose_name='所具有的权限', blank=True)

    class Meta:
        verbose_name_plural = '角色表'

    def __str__(self):
        return self.rolename


class Permission(models.Model):
    '''权限表'''
    title = models.CharField(max_length=32, verbose_name='权限名')
    url = models.CharField(max_length=64, verbose_name='含正则url')
    is_menu = models.BooleanField(verbose_name='是否为菜单')

    class Meta:
        verbose_name_plural = '权限表'

    def __str__(self):
        return self.title
