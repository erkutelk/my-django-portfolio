from django.shortcuts import render # type: ignore
from . import views
from django.urls import path # type: ignore
from django.contrib import admin # type: ignore
from django.urls import path,include # type: ignore
from django.conf.urls.static import static # type: ignore
from django.conf import settings # type: ignore
urlpatterns=[
    path('login',views.user_login,name='login'),
    path('logout',views.user_login,name='logout'),
]
