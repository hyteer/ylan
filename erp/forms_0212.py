# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.forms import ModelForm
from models import Customer,Role
from django.contrib.auth.models import User

class PostForm(forms.Form):
    post_text = forms.CharField(label='Your Post', max_length=100)


class CustForm(ModelForm):

    class Meta:
        model = Customer
        fields = ['id','user','role','name', 'phone', 'email','country']
        widgets = {
            'user': forms.TextInput(attrs={'required': True,'placeholder':'用户名'}),
        }
    def clean_username(self): # check if username dos not exist before
        try:
            User.objects.get(username=self.cleaned_data['user']) #get user from user model
        except User.DoesNotExist :
            return self.cleaned_data['user'].pk

        raise forms.ValidationError("this user exist already")
    def clean(self):
        cleaned_data=super(CustForm,self).clean()
        username=cleaned_data.get('username')
        name=cleaned_data.get('name')
        phone = cleaned_data.get('phone')
        email = cleaned_data.get('email')

        if not user:
            self._errors['user'] = self.error_class([u"请输入用户名!"])
        if not name:
            self._errors['name'] = self.error_class([u"请输入姓名!"])
        if not phone:
            self._errors['phone'] = self.error_class([u"请输入电话!"])
        return cleaned_data


class UserForm(forms.Form):
    style_class = {'class':'form-control'}
    username = forms.CharField(label='账号',max_length=20,widget=forms.TextInput(attrs=style_class))
    #password = forms.CharField(label='密码', widget=forms.PasswordInput())
    password = forms.CharField(required=True,label='密码', widget=forms.PasswordInput(attrs=style_class),
                          min_length=6,
                          max_length=10,
                          error_messages={'required': '密码不能为空.', 'min_length': "至少6位"})
    confirm_password = forms.CharField(required=True,label='确认密码', \
    widget=forms.PasswordInput(attrs=style_class),
                          min_length=6,
                          max_length=10,
                          error_messages={'required': '密码不能为空.', 'min_length': "至少6位"})
    def clean(self):
        cleaned_data=super(UserForm,self).clean()
        username= cleaned_data.get('username')
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if not username:
            self._errors['username'] = self.error_class([u"请输入用户名!"])
        if not password:
            self._errors['password'] = self.error_class([u"请输入密码!"])
        if password != confirm_password:
            raise forms.ValidationError(u'Passwords are not equal')
        return self.cleaned_data

        #return cleaned_data


class RoleForm(ModelForm):
    class Meta:
        model = Role
        fields = ['role_type', 'name']

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class AddCustomerForm(forms.Form):
    username = forms.CharField(label='登录账号',max_length=20)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    name = forms.CharField(label='姓名',max_length=30)
    phone = forms.CharField(max_length=20,error_messages={'required': '数字不能空.', 'invalid': '必须输入数字'})
    email = forms.EmailField()
    remark = forms.CharField(widget=forms.Textarea)


class CustomerForm(forms.Form):
    style_class = {'class':'form-control'}
    username = forms.CharField(label='账号',max_length=20,widget=forms.TextInput(attrs=style_class))
    #password = forms.CharField(label='密码', widget=forms.PasswordInput())
    password = forms.CharField(required=True,label='密码', widget=forms.PasswordInput(attrs=style_class),
                          min_length=6,
                          max_length=10,
                          error_messages={'required': '密码不能为空.', 'min_length': "至少6位"})
    confirm_password = forms.CharField(required=True,label='确认密码', \
    widget=forms.PasswordInput(attrs=style_class),
                          min_length=6,
                          max_length=10,
                          error_messages={'required': '密码不能为空.', 'min_length': "至少6位"})

    name = forms.CharField(required=False,label='姓名',max_length=30,widget=forms.TextInput(attrs=style_class))
    phone = forms.CharField(required=False,label='电话',max_length=20,error_messages=\
    {'required': '数字不能空.', 'invalid': '必须输入数字'},widget=forms.TextInput(attrs=style_class))
    #email = forms.EmailField()
    #remark = forms.CharField(widget=forms.Textarea)
    def clean_username(self): # check if username dos not exist before
        try:
            User.objects.get(username=self.cleaned_data['username']) #get user from user model
        except User.DoesNotExist :
            return self.cleaned_data['username']

        raise forms.ValidationError("this user exist already")

    def clean(self):
        cleaned_data=super(CustomerForm,self).clean()
        username= cleaned_data.get('username')
        password = cleaned_data['password']
        confirm_password =cleaned_data['confirm_password']

        if not username:
            self._errors['username'] = self.error_class([u"请输入用户名!"])
        if not password:
            self._errors['password'] = self.error_class([u"请输入密码!"])
        if password != confirm_password:
            raise forms.ValidationError(u'Passwords are not equal')
        return self.cleaned_data

    def save(self): # create new user
        customer = Customer(name=name,phone=phone)
        new_user=User.objects.create_user(username=self.cleaned_data['username'],
                                        password=self.cleaned_data['password'],
                                        customer=customer)

        return new_user


class CustomerForm2(forms.Form):
    username = forms.CharField(label='账号',max_length=20)
    #password = forms.CharField(label='密码', widget=forms.PasswordInput())
    password = forms.CharField(required=True,label='密码', widget=forms.PasswordInput(),
                          min_length=6,
                          max_length=10,
                          error_messages={'required': '密码不能为空.', 'min_length': "至少6位"})
    password2 = forms.CharField(required=True,label='确认密码', widget=forms.PasswordInput(),
                          min_length=6,
                          max_length=10,
                          error_messages={'required': '密码不能为空.', 'min_length': "至少6位"})
    name = forms.CharField(required=False,label='姓名',max_length=30)
    phone = forms.CharField(label='电话',max_length=20,error_messages={'required': '数字不能空.', 'invalid': '必须输入数字'})
    #email = forms.EmailField()
    #remark = forms.CharField(widget=forms.Textarea)

    def clean_user(self):
        username = self.cleaned_data.get('username')
        if username == 'cc':
            raise forms.ValidationError('用户名是我的!')
        return username

    def clean(self):
        cleaned_data = self.cleaned_data
        pwd = cleaned_data['password']
        pwd2 = cleaned_data['password2']
        #print(pwd,pwd2)
        if pwd != pwd2:
            raise forms.ValidationError('二次输入密码不匹配')
        return cleaned_data
