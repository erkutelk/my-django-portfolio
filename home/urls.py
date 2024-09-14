from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('',views.home_),
    path('home', views.home_,name='anasayfa'),
    path('about',views.about),
    path('blog/<str:slug>',views.detay, name='detay')
    
]
