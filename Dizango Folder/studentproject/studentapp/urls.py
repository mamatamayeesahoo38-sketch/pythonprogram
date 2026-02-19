from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('welcome/', views.welcome, name='welcome'),
    path('password_change/', views.change_password, name='password_change'),
]
