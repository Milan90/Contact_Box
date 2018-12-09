"""Skrzynka_kontaktowa_warsztat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from contact_box.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^new/$', AddPerson.as_view()),
    re_path(r'^modify/(?P<id>\d+)$', EditPerson.as_view()),
    re_path(r'^delete/(?P<id>\d+)$', DeletePerson.as_view()),
    re_path(r'^show/(?P<id>\d+)$', ShowPerson.as_view()),
    re_path(r'^$', ShowPersonList.as_view()),
    re_path('^(?P<id>\d+)/addAddress$', addAddress.as_view()),
    re_path(r'^delPhone/(?P<id>\d+)$', DelPhone.as_view()),
    re_path(r'^(?P<id>\d+)/addPhone$', AddPhone.as_view()),
]
