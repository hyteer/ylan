from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30,null=True, blank=True)
    phone = models.CharField(blank=True, max_length=20,null=True)
    email = models.EmailField(blank=True,null=True)
    address = models.CharField(max_length=100,null=True, blank=True)
    district = models.CharField(max_length=30,null=True, blank=True)
    country = models.ForeignKey("Country", null=True, blank=True)
    remark = models.TextField(blank=True, null=True)
    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.user.username

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(blank=True, max_length=20,null=True)
    address = models.CharField(blank=True, max_length=80, null=True)
    email = models.EmailField(blank=True,null=True)
    zipcode = models.CharField("ZipCode", max_length=80, null=True, blank=True)
    country = models.ForeignKey("Country", null=True, blank=True)
    remark = models.TextField(blank=True, null=True)
    def __str__(self):
		return self.name


class Country(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
		return self.name
