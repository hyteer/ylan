# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required

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
    return render(req, 'erp/test.html')

def user_login(req):
    if req.method == 'POST':
        #messages.info(req, '欢迎登录使用!')
        #import pdb; pdb.set_trace()
        #return HttpResponseRedirect('/erp')
        #return render(req, 'erp/starter.html')

		#form = LoginForm(req.POST)

        username = req.POST['username']
        password = req.POST['password']
        #username = form.cleaned_data['username']
        #password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if req.user.is_superuser == True:
            usertype = 99
        else:
            user_type = userTypes[user.groups.all().first().name]


        if user is not None:
            login(req, user)
            req.session['usertype'] = user_type
            #req.session.save()
            return HttpResponseRedirect('/erp')
            #return render(req, 'erp/starter.html')
        else:
            return HttpResponse('Invalid login.')

    else:
        #form = LoginForm()
        #return render(req, 'crm/login.html', {'form': form})
        return render(req, 'erp/login.html')

def user_logout(req):
    logout(req)
    return HttpResponseRedirect('/erp/login')

def register(req):
	return render(req, 'erp/register.html')

@login_required(redirect_field_name='/erp/login')
def customer(req):
    #import pdb; pdb.set_trace()
    return render(req, 'erp/customer.html')

@login_required(redirect_field_name='/erp/login')
def consign(req):
    return render(req, 'erp/consign.html')
