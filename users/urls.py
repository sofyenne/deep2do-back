from django.contrib import admin
from django.urls import path 
from .views import *



urlpatterns = [
    
    path('register' , register.as_view()),
    path('login' , login.as_view()),
    path('user' , getuser().as_view()),
    path('logout' , logout().as_view()),
    path('contact' , contact.as_view()),
    path('users' , alluser().as_view()),
    path('users/<int:pk>' , usercrud().as_view()),
   
   
]