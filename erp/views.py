# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from .forms import NameForm, ContactForm, AddCustomerForm
from .models import Customer

userTypes = {
    'guests':0,
    'customers':1,
    'users':2,
    'managers':3,
    'super':99
}

# Create your views here.
@login_required(redirect_field_name='/erp/login')
def index(req):
    #import pdb; pdb.set_trace()
    return render(req, 'erp/index.html')

@login_required(redirect_field_name='/erp/login')
def test(req):
    #import pdb; pdb.set_trace()
    if req.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(req.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            return HttpResponseRedirect('/thanks/')
    else:
        nameform = NameForm()
        contactform = ContactForm()
    #return render(req, 'erp/test.html',{'nameform':nameform,'form':contactform})
    return render(req, 'erp/bootsdemo.html',{'form':nameform})

#### 用户登录 ####
def user_login(req):
    if req.method == 'POST':

        username = req.POST['username']
        password = req.POST['password']
        #username = form.cleaned_data['username']
        #password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and hasattr(user,'customer'):
            if user.customer.status == 0:
                return HttpResponse('账号已经停用')
            else:
                login(req, user)
                return HttpResponseRedirect('/erp')
        else:
            return HttpResponse('Invalid login.')
    else:

        return render(req, 'erp/login.html')

def user_logout(req):
    logout(req)
    return HttpResponseRedirect('/erp/login')

def register(req):
	return render(req, 'erp/register.html')

def userinfo(req):
    if req.method == 'POST':
        return HttpResponse('test....')
    else:
        return HttpResponse('recieved your request.')

#### 客户管理页 ####
@login_required(redirect_field_name='/erp/login')
def customer(req):
    cutomers = Customer.objects.all()
    form = AddCustomerForm()
    return render(req, 'erp/customer.html',{'customers':cutomers,'form':form})

#### 添加客户 ####
@login_required(redirect_field_name='/erp/login')
def add_customer(req):
    if req.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddCustomerForm(req.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            return HttpResponseRedirect('/thanks/')
    return render(req, 'erp/customer.html')

@login_required(redirect_field_name='/erp/login')
def consign(req):
    return render(req, 'erp/consign.html')
