"""permission URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views as app01_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', app01_views.login),
    url(r'^index/$', app01_views.index),
    url(r'^userinfo/$', app01_views.userinfo),
    url(r'^userinfo/add/$', app01_views.userinfo_add),
    url(r'order/', app01_views.order),
    url(r'^order/add/$', app01_views.order_add),

]