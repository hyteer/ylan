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
    phone = forms.CharField(max_length=20,error_messages={'required': '数字不能空.', 'invalid': '必须输入数字'})
    email = forms.EmailField()
    remark = forms.CharField(widget=forms.Textarea)

class CustomerForm(forms.Form):
    useracc = forms.CharField(label='账号',max_length=20)
    #password = forms.CharField(label='密码', widget=forms.PasswordInput())
    password = forms.CharField(required=True,label='密码', widget=forms.PasswordInput(),
                          min_length=6,
                          max_length=10,
                          error_messages={'required': '密码不能为空.', 'min_length': "至少6位"})
    password2 = forms.CharField(required=True,label='密码', widget=forms.PasswordInput(),
                          min_length=6,
                          max_length=10,
                          error_messages={'required': '密码不能为空.', 'min_length': "至少6位"})
    name = forms.CharField(label='姓名',max_length=30)
    phone = forms.CharField(max_length=20,error_messages={'required': '数字不能空.', 'invalid': '必须输入数字'})
    #email = forms.EmailField()
    #remark = forms.CharField(widget=forms.Textarea)

    def clean_user(self):
        useracc = self.cleaned_data.get('useracc')
        if useracc == 'cc':
            raise forms.ValidationError('用户名是我的!')
        return useracc

    def clean(self):
        cleaned_data = self.cleaned_data
        pwd = cleaned_data['password']
        pwd2 = cleaned_data['password2']
        #print(pwd,pwd2)
        if pwd != pwd2:
            raise forms.ValidationError('二次输入密码不匹配')
        return cleaned_data
