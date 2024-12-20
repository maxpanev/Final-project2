from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('layoute', views.layoute, name='layoute'),
    path('home/', views.home, name='home'),
    path('basket/', views.basket, name='basket'),
    path('add_to_basket/<int:product_id>/', views.add_to_basket, name='add_to_basket'),
    path('basket/remove/<int:item_id>/', views.remove_from_basket, name='remove_from_basket'),
    path('checkout/', views.checkout, name='checkout'),
    path('story/', views.story_view, name='story'),
]