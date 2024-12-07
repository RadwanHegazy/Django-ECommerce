from . import views
from django.urls import path

urlpatterns = [
    path('auth/login/',views.LoginView.as_view(),name='auth_login'),
    path('auth/register/',views.RegisterView.as_view(),name='auth_register'),
    path('profile/change-password/',views.ChangePassword.as_view(), name='change_password'),
    path('auth/forget-password/',views.ResetPasswordOTP.as_view(),name='sent_otp_email'),
    path('auth/forget-password/reset/', views.ResetPassowrd.as_view(),name='reset_passowrd'),
    path('profile/', views.ProfileView.as_view(),name='profile'),
]