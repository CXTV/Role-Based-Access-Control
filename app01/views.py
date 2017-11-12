import re
from django.shortcuts import render, HttpResponse, redirect
from rbac import models
from rbac.service.init_permission import init_permission


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pwd')
        user = models.User.objects.filter(username=username, password=password).first()
        if user:
            init_permission(user, request)
            return redirect('/index')

        return render(request, 'login.html')

    return render(request, 'login.html')


def index(request):
    # current_url = request.path_info
    # permission_list = request.session.get('permission_url')
    # if permission_list:
    #     flag = False
    #     for url in permission_list:
    #         regex = '^{0}$'.format('url')
    #         if re.match(regex,current_url):
    #             flag = True
    #             break
    #
    #     if not flag:
    #         return HttpResponse('无权访问')
    #
    # return redirect('/login/')

    return HttpResponse('欢迎登陆')


def index(request):
    return HttpResponse('欢迎登录')


def userinfo(request):
    return HttpResponse('用户列表页面')


def userinfo_add(request):
    return HttpResponse('添加用户页面')


def order(request):
    return HttpResponse('订单列表页面')


def order_add(request):
    return HttpResponse('添加订单页面')
