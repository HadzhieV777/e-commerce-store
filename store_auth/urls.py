from django.urls import path, reverse_lazy
from django.views.generic import RedirectView
from .views import UserLoginView, UserRegisterView, UserLogoutView, ChangePasswordView, PasswordChangedView, RegisteredView

from .forms import SetNewPasswordForm, ResetPasswordForm
from django.contrib.auth import views as auth_views


urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='user register'),
    path('login/', UserLoginView.as_view(), name='user login'),
    path('logout/', UserLogoutView.as_view(), name='user logout'),
    
    # Change Password
    path('change_password/', ChangePasswordView.as_view(), name='change password'),
    path('password_changed/', PasswordChangedView.as_view(), name='password changed'),
    path('password_change_done/', RedirectView.as_view(url=reverse_lazy('password changed')), name='password_change_done'),
    path('successfully_registered/', RegisteredView.as_view(), name='successfully registered'),
    
    # Forgotten Password
    path('reset_password/', 
         auth_views.PasswordResetView.as_view(form_class=ResetPasswordForm ,template_name="store_auth/forgotten_password/reset_password.html"),
         name='reset_password'),
    
    path('reset_password_sent/', 
         auth_views.PasswordResetDoneView.as_view(template_name="store_auth/forgotten_password/password_reset_done.html"),
         name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(form_class=SetNewPasswordForm ,template_name="store_auth/forgotten_password/password_reset_confirm.html"),
         name='password_reset_confirm'),
    
    path('reset_password_complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name="store_auth/forgotten_password/password_reset_complete.html"),
         name='password_reset_complete'),
)
