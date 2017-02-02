# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Customer,Role, Contact,Country

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    fieldsets = [
    	(None, {'fields': ['name']}),
        ('关联用户', {'fields': ['user']}),
        ('角色', {'fields': ['role']}),
    	('电话', {'fields': ['phone']}),
    	('Email', {'fields': ['email']}),
    	('地址', {'fields': ['address']}),
        ('Status', {'fields': ['status']}),
    	('备注', {'fields': ['remark'], 'classes': ['collapse']}),
    	('Country', {'fields': ['country']}),
    ]
    #inlines = ('客户类型', {'fields':[FollowRecordsInline]})
    #inlines = [FollowRecordsInline]
    list_display = ('display_name', 'user', 'role_name', 'phone', 'email', 'country','status')
    #fields = ['question_text','pub_date']
    list_filter = ['country']
    search_fields = ['name']



# Define an inline admin descriptor for Customer model
# which acts a bit like a singleton
class CustomerInline(admin.StackedInline):
    model = Customer
    can_delete = False
    verbose_name_plural = 'customers'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (CustomerInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Role)
admin.site.register(Contact)
admin.site.register(Country)
