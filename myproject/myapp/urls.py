from django.urls import path
from . import views

urlpatterns = [
    path('', views.layoute, name='layoute'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('click/', views.click, name='click'),
]