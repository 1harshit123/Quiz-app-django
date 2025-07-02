
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
    path('login/', views.user_login, name = 'login'),
    path('', views.home, name = 'home'),
    path('create_quiz/', views.create_quiz, name = 'create_quiz')
]
