from django.contrib import admin
from django.urls import path, include
from bloodbank import views

urlpatterns = [
    path('', views.index, name="login"),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('NGOform', views.ngoform, name="ngoform"),
    path('user', views.user, name="user"),
    path('Hospitalform', views.hospitalform, name="hospitalform"),
    path('Bloodbankform', views.bloodbankform, name="bloodbank"),
    path('Userform', views.userform, name="userform"),
    path('hospitalinterface', views.hospitalInterface)
    
]
