# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from . import views

app_name = 'erp'  # set this app's namespace

urlpatterns = [
    url(r'^$', views.index, name='home'),
    #url(r'^formset$', DefaultFormsetView.as_view(), name='formset_default'),


]
