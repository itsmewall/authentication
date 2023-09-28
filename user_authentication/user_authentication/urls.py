from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  
from usersapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(), name='login'),  # Use a view de login padrão do Django
    path('register/', views.register, name='register'),
    path('profile/', views.user_profile, name='profile'),
]
