# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'erp'  # set this app's namespace

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^test/$', views.test, name='test'),
    url(r'^login2/$', auth_views.login),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^lockscreen/$', views.lockscreen, name='lockscreen'),
    url(r'^customer/$', views.customer, name='customer'),
    url(r'^customer_add/$', views.customer_add, name='customer_add'),
    url(r'^customer_del/$', views.customer_del, name='customer_del'),
    url(r'^customer_edit/$', views.customer, name='customer'),
    url(r'^consign/$', views.consign, name='consign'),
    url(r'^userinfo/$', views.userinfo, name='userinfo'),

]
