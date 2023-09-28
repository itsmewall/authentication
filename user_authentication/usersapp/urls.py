from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView
from django.contrib.auth.views import PasswordChangeView

app_name = "usersapp"

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.user_profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),

]
