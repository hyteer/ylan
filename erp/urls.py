# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'erp'  # set this app's namespace

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^test/$', views.test, name='test'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^custinfo/(?P<username>[a-z]+)/$', views.custinfo, name='custinfo'),
    url(r'^trans_test/$', views.trans_test, name='trans_test'),
    url(r'^ajax_test/$', views.ajax_test, name='ajax_test'),
    url(r'^create_post/$', views.create_post, name='create_post'),
    url(r'^login2/$', auth_views.login),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^set_password/$', views.set_password, name='set_password'),
    url(r'^lockscreen/$', views.lockscreen, name='lockscreen'),
    url(r'^customer/$', views.customer, name='customer'),
    url(r'^customer_add/$', views.customer_add, name='customer_add'),
    url(r'^customer_del/$', views.customer_del, name='customer_del'),
    url(r'^customer_edit/$', views.customer_edit, name='customer_edit'),
    url(r'^consign/$', views.consign, name='consign'),
    url(r'^userinfo/$', views.userinfo, name='userinfo'),

]
