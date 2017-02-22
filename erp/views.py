# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json,time,datetime
from django.shortcuts import render,HttpResponseRedirect, get_object_or_404, \
render_to_response
from django.http import HttpResponse
from django.template import loader, Context
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from django.contrib.messages import constants as messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import NameForm, ContactForm, CustomerForm,AddCustomerForm,UserForm, \
CustForm, PostForm, RegisterForm
from django.contrib.auth.models import User
from django.db import transaction,IntegrityError
from .models import Customer,Role



userTypes = {
    'guests':0,
    'customers':1,
    'users':2,
    'managers':3,
    'super':99
}

DEFAULT_ROLE = Role.objects.get(role_type=1)

# Create your views here.
@login_required(redirect_field_name='/erp/login')
def index(req):
    #import pdb; pdb.set_trace()
    form = PostForm()
    return render(req, 'erp/index.html',{'form':form})

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

######################用户登录 ##################
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
                messages.add_message(req, messages.INFO, 'Login Successful.')
                return HttpResponseRedirect('/erp')
        else:
            return HttpResponse('Invalid login.')
    else:

        return render(req, 'erp/pages/login.html')

def user_logout(req):
    logout(req)
    #import pdb; pdb.set_trace()
    messages.add_message(req, messages.INFO, 'Signout Successful.')
    return HttpResponseRedirect('/erp/login')


# 用户注册
@transaction.atomic
def register(req):
    resp = {"error":0,"msg":"收到消息!"}
    if req.method == 'POST':
        import pdb; pdb.set_trace()
        print("Recieved a post request...")
        #print("Data:%s" % req.body)

        data = json.loads(req.body)

        try:
            with transaction.atomic():
                user = User.objects.create_user(username=data['username'],password=data['password'])
                cust = Customer.objects.create(user=user,role=DEFAULT_ROLE,email = data['email'])
                cust.save()
                print("saved customer...")
                resp['msg'] = '注册成功，即将跳转到登录界面！'
                resp = json.dumps(resp)
                return HttpResponse(resp)
        except IntegrityError:
            print("There is an IntegrityError...")
            resp['error'] = 4000
            resp['msg'] = '数据库错误！'
            return HttpResponse(resp)

    else:
        form = RegisterForm()
        return render(req, 'erp/pages/register.html',{'form':form})
        #return render(req, 'erp/pages/register.html')

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


########################### 用户管理 ###########################

@login_required(redirect_field_name='/erp/login')
def setting(req):
    return render(req, 'erp/pages/setting.html')

@login_required(redirect_field_name='/erp/login')
def product(req):
    return render(req, 'erp/pages/product.html')

#### 客户管理页 ####
@login_required(redirect_field_name='/erp/login')
def customer(req):
    cutomer_list = Customer.objects.all()
    paginator = Paginator(cutomer_list,16)
    #userform = UserForm(prefix='user')
    #form = CustomerForm()
    custform = CustForm(prefix='cust')
    page = req.GET.get('page')
    try:
        customers = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        customers = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        customers = paginator.page(paginator.num_pages)
    return render(req, 'erp/customer/index.html', {'customers': customers,'custform':custform})

@login_required(redirect_field_name='/erp/login')
def custlist(req):
    cutomer_list = Customer.objects.all()
    paginator = Paginator(cutomer_list,16)
    #userform = UserForm(prefix='user')
    #form = CustomerForm()
    custform = CustForm(prefix='cust')
    page = req.GET.get('page')
    try:
        customers = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        customers = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        customers = paginator.page(paginator.num_pages)
    return render(req, 'erp/customer/index.html', {'customers': customers,'custform':custform})

#### 添加用户 ####
@transaction.atomic
@login_required(redirect_field_name='/erp/login')
def customer_add(req):
    if req.method == 'POST':
        #import pdb; pdb.set_trace()
        #form = UserForm(req.POST)
        #form = CustomerForm(req.POST)
        form = CustForm(req.POST,prefix='cust')

        if form.is_valid():

            print("Post Data:",form.cleaned_data)
            #import pdb; pdb.set_trace()
            if form.save():
                print("Created a new user...")
                return HttpResponse('{"code":0,"msg":"created..."}')
        else:
            #import pdb; pdb.set_trace()
            errors = {'errors':form.errors['__all__']}
            print(errors)
            return HttpResponse('{"code":11,"errors":errors}')

    else:
        return HttpResponse("非法请求!")

# 修改密码
@transaction.atomic
def set_password(req):
    #import pdb; pdb.set_trace()
    data = json.loads(req.body)
    user = get_object_or_404(User, username=data['username'])
    from .utils import test_password
    if not user.check_password(data['password']):
        return HttpResponse('{"error":1,"msg":"密码错误！"}')
    if data['new_password'] != data['confirm_password']:
        return HttpResponse('{"error":1,"msg":"两次密码输入不一致！"}')
    if not test_password(data['new_password']):
        return HttpResponse('{"error":1,"msg":"密码不符合要求！"}')

    try:
        with transaction.atomic():
            user.set_password(data['new_password'])
            user.save()
    except IntegrityError:
        print("There's an error...")
    #import pdb; pdb.set_trace()
    return HttpResponse('{"error":0,"msg":"密码修改成功，请重新登录！"}')


#@csrf_exempt
@transaction.atomic
@login_required(redirect_field_name='/erp/login')
def custinfo(req,username):
    user = get_object_or_404(User, username=username)

    if req.method=="POST":
        print("user:",username)
        user = get_object_or_404(User, username=username)
        #import pdb; pdb.set_trace()
        role = Role.objects.filter(pk=req.POST['role']).first()
        cust = get_object_or_404(Customer, user=user)
        #try:
        try:
            with transaction.atomic():
                #user.save()
                #print("saved user...")
                cust.email = req.POST['email']
                cust.phone = req.POST['phone']
                cust.save()
                print("saved customer...")
                return HttpResponse("Post response: hi %s !" % username)
        except IntegrityError:
            print("There is an IntegrityError...")
            return HttpResponse("There is an IntegrityError！")

    else:
        user = get_object_or_404(User, username=username)
        #import pdb; pdb.set_trace()
        cust = get_object_or_404(Customer, name=user.customer.name)
        custform = CustForm(instance=cust)
        return render(req,'erp/customer/custinfo.html',{'user':user,'form':custform})
        #return HttpResponse("Hi %s !" % username)

@csrf_exempt
def userinfo(req):
    #username = req.GET['username']
    if req.method=="POST":
        #import pdb; pdb.set_trace()
        custer = get_object_or_404(Customer,)
        form=UserForm(req.POST,instance=custer)
        import pdb;pdb.set_trace()
        if form.is_valid():
            user=form.save()
            #blog.save()
            return HttpResponseRedirect(reverse("customer"))
    else:
        cusid = req.GET['id']
        #user=get_object_or_404(User,username=username)
        custer = get_object_or_404(Customer,pk=cusid)
        return render_to_response('erp/customer/boot.html', {'form': CustForm(instance=custer)})

#### 编辑用户 ####
@login_required(redirect_field_name='/erp/login')
def customer_edit(req):
    if req.method == 'POST':
        import pdb; pdb.set_trace()
        print("Data:",req.body)
        return HttpResponse("已收到.\nData:"+req.body)
        #import pdb; pdb.set_trace()
        '''
        if form.is_valid():
            print("Post Data:",form.cleaned_data)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            user = User.objects.create_user(username=username, password=password)
            customer = Customer(user=user,name=name,phone=phone,role_id=1)
            customer.save()
            # process the data in form.cleaned_data as required
            data = {"code":"1","msg":"success!"}
            data = json.dumps(data)
            return HttpResponse(data)
        '''
    else:
        return HttpResponse("非法请求!")

####  删除用户 ####
@login_required(redirect_field_name='/erp/login')
def customer_del(req):
    if req.method == 'POST':
        #import pudb; pudb.set_trace()
        print("Data:",req.body)
        data = json.loads(req.body)
        print("name:",data['username'])
        user = User.objects.filter(username=data['username']).first()
        user.delete()
        return HttpResponse('{"code":0,"msg":"删除成功！"}')

    else:
        return HttpResponse("非法请求!")

@login_required(redirect_field_name='/erp/login')
def consign(req):
    return render(req, 'erp/consign.html')




######################### Test&Debug #############################
#@csrf_exempt
def django_ajax(req):
    #import pdb; pdb.set_trace()
    c = 2 + 3
    #html = render('erp')
    wd = loader.get_template('erp/components/widget.html')
    html = wd.render()
    #return HttpResponse('{"result": "erp/consign.html"}')
    #return render(req, 'erp/components/widget.html')
    #return HttpResponse(html)
    return render_to_response('erp/components/widget.html')


@transaction.atomic
def trans_test(request):
    create_parent()

    try:
        with transaction.atomic():
            generate_relationships()
    except IntegrityError:
        handle_exception()

    add_children()

def create_post(request):
    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        response_data = {}
        print("Post Text:",request.body)

        #post = Post(text=post_text, author=request.user)
        #post.save()

        #response_data['result'] = 'Create post successful!'
        #response_data['postpk'] = post.pk
        #response_data['text'] = post.text
        #response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
        #response_data['author'] = post.author.username
        #custer = get_object_or_404(Customer,name=post_text)
        response_data['result'] = 'Create post successful!'
        response_data['postpk'] = '11'
        response_data['text'] = post_text
        response_data['created'] = str(datetime.datetime.now())
        response_data['author'] = 'YT'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

@csrf_exempt
def temptest(req):
    if req.method == 'POST':
        return HttpResponse('{"code":1,"msg":"ok"}')
    else:
        return HttpResponse('wrong request...')

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

# Model Form View
@csrf_exempt
def ajax_test2(req):
    if req.method=="POST":
        print("Data:",req.body)
        return HttpResponse("已收到.\nData:"+req.body)
            #return HttpResponseRedirect(reverse("customer"))
    else:
        return HttpResponse("非法请求!")

@csrf_exempt
def ajax_test(req):
    if req.method=="POST":
        #import pdb; pdb.set_trace()
        resp = {"code":1,"msg":"ok"}
        data = req.body
        resp['msg'] = str(data)
        resp = json.dumps(resp)
        print("Data:",data)
        #print("Data received:",req.body)
        return HttpResponse(resp)
            #return HttpResponseRedirect(reverse("customer"))
    else:
        return HttpResponse("非法请求!")
