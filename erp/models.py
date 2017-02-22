# -*- coding: utf-8 -*-


from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, primary_key=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=30,null=True, blank=True)
    role = models.ForeignKey("Role")
    phone = models.CharField(blank=True, max_length=20,null=True)
    email = models.EmailField(blank=True,null=True)
    address = models.CharField(max_length=100,null=True, blank=True)
    district = models.CharField(max_length=30,null=True, blank=True)
    country = models.ForeignKey("Country", null=True, blank=True)
    status = models.IntegerField(default=0)
    remark = models.TextField(blank=True, null=True)
    def __unicode__(self):
        if self.name:
            return self.name
        else:
            return self.user.username
    def display_name(self):
        return self.name
    def role_name(self):
        return self.role.name
    def status_name(self):
        if self.status == 0:
            return '未激活'
        elif self.status == 2:
            return '禁用'
        elif self.status == 1:
            return '正常'
        else:
            return '异常'
    display_name.short_description = '姓名'
    role_name.short_description = '角色'
    def get_customer_info(self):
        data = {'user':self.user.username,'user_id':self.user.pk,'name':self.name,\
            'phone':self.phone,'email':self.email
        }
        return data

class Role(models.Model):
    role_type = models.IntegerField()
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"
    def display_name(self):
        return self.name
    display_name.short_description = '角色'
    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(blank=True, max_length=20,null=True)
    address = models.CharField(blank=True, max_length=80, null=True)
    email = models.EmailField(blank=True,null=True)
    zipcode = models.CharField("ZipCode", max_length=80, null=True, blank=True)
    country = models.ForeignKey("Country", null=True, blank=True)
    remark = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name



class Country(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"
