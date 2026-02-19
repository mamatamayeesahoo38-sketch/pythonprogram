from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('studentapp.urls')),

    # Password Reset
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='studentapp/password_reset.html'),
         name='password_reset'),
]
