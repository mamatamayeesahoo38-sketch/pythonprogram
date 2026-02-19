from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_student, name='add'),
    path('show/', views.show_students, name='show'),
    path('update/<int:id>/', views.update_student, name='update'),
    path('delete/<int:id>/', views.delete_student, name='delete'),
]
