from django.contrib import admin
from django.urls import path, include   # ✅ IMPORTANT
from django.contrib.auth import views as auth_views  # if using login

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/login/',
         auth_views.LoginView.as_view(template_name='cartapp2/login.html'),
         name='login'),

    path('accounts/logout/',
         auth_views.LogoutView.as_view(next_page='/'),
         name='logout'),

    path('', include('cartapp2.urls')),
]
