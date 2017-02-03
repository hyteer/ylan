# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import NameForm, ContactForm, CustomerForm,AddCustomerForm
from django.contrib.auth.models import User
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

        return render(req, 'erp/pages/login.html')

def user_logout(req):
    logout(req)
    return HttpResponseRedirect('/erp/login')

def register(req):
	return render(req, 'erp/pages/register.html')

@login_required
def lockscreen(req):
    return render(req, 'erp/pages/lockscreen.html')


@login_required
def second_auth(req):
    if req.method == 'POST':
        user = authenticate(username=username, password=password)
        if user:
            return HttpResponse('{"code":0,"msg":"ok"}')
        else:
            return HttpResponse('{"code":4003,"msg":"auth fails"}')



@csrf_exempt
def userinfo(req):
    if req.method == 'POST':
        return HttpResponse('{"code":1,"msg":"ok"}')
    else:
        return HttpResponse('wrong request...')

#### 客户管理页 ####
@login_required(redirect_field_name='/erp/login')
def customer(req):
    cutomers = Customer.objects.all()
    form = CustomerForm()
    return render(req, 'erp/customer.html',{'customers':cutomers,'form':form})

#### 添加用户 ####
@login_required(redirect_field_name='/erp/login')
def customer_add(req):
    if req.method == 'POST':
        form = CustomerForm(req.POST)
        #import pdb; pdb.set_trace()
        if form.is_valid():
            print "Post Data:",form.cleaned_data
            useracc = form.cleaned_data['useracc']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            user = User.objects.create_user(username=useracc, password=password)
            customer = Customer(user=user,name=name,phone=phone,role_id=1)
            customer.save()
            # process the data in form.cleaned_data as required
            data = {"code":"1","msg":"success!"}
            data = json.dumps(data)
            return HttpResponse(data)
    else:
        return HttpResponse("非法请求!")

#### 删除用户 ####
@login_required(redirect_field_name='/erp/login')
def customer_del(req):
    if req.method == 'POST':
        #import pudb; pudb.set_trace()
        print "Data:",req.POST
        return HttpResponse("已收到请求")

    else:
        return HttpResponse("非法请求!")

@login_required(redirect_field_name='/erp/login')
def consign(req):
    return render(req, 'erp/consign.html')
