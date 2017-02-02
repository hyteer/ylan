# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class AddCustomerForm(forms.Form):
    useracc = forms.CharField(label='登录账号',max_length=20)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    name = forms.CharField(label='姓名',max_length=30)
    phone = forms.CharField(max_length=20)
    email = forms.EmailField()
    remark = forms.CharField(widget=forms.Textarea)
