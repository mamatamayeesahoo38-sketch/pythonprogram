from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/<int:id>/', views.add_to_cart, name='add'),
    path('cart/', views.cart, name='cart'),
    path('remove/<int:id>/', views.remove_item, name='remove'),
    path('update/<int:id>/', views.update_quantity, name='update'),
    path('checkout/', views.checkout, name='checkout'),
]
