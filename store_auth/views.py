from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import UserLoginForm, UserRegisterForm, ChangePasswordForm
from django.contrib.auth import login, logout
from django.views import generic as views


class UserRegisterView(views.CreateView):
    form_class = UserRegisterForm
    template_name = 'store_auth/user_register.html'
    success_url = reverse_lazy('successfully registered')
    
    def form_valid(self, form):
        user = form.save()
        login(
            self.request,
            user,)
        return redirect(self.success_url)


class UserLoginView(auth_views.LoginView):
    form_class = UserLoginForm
    template_name = 'store_auth/user_login.html'
    success_url = reverse_lazy('homepage')
   
    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(views.View):
    def get(self, request):
        logout(request)
        return redirect(reverse_lazy('homepage'))
    

class ChangePasswordView(auth_views.PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'store_auth/change_password.html'

    
class PasswordChangedView(views.TemplateView):
    template_name = 'store_auth/redirect_pages/password_changed.html'


class RegisteredView(views.TemplateView):
    template_name = 'store_auth/redirect_pages/registered.html'        
    
    