from django.urls import path
from . import views

urlpatterns = [
    path('', views.input_page, name='input'),
    path('result', views.result_page, name='result'),
]
