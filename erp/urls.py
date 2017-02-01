# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'erp'  # set this app's namespace

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^login2/$', auth_views.login),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
]
