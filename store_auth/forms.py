from django.contrib.auth import forms as auth_forms
from core_helpers.form_mixins import FormFieldsController
from django.contrib.auth.password_validation import validate_password
from core_helpers.validators import validate_password_contains_uppercase_letter, validate_password_contains_lowercase_letter, validate_password_contains_digit, validate_password_contains_special_symbol
from django import forms
from .models import StoreUser


class UserRegisterForm(auth_forms.UserCreationForm, FormFieldsController):
    class_name = "form-control"
    help_text_to_remove = "__all__"
    placeholders = {
        "email": "Email address",
        "password1": "Enter Password",
        "password2": "Confirm password"
    }
    more_validators = {
        "password2": [
            validate_password,
            validate_password_contains_uppercase_letter, 
            validate_password_contains_lowercase_letter, 
            validate_password_contains_digit, 
            validate_password_contains_special_symbol,
        ]
    }
    
    class Meta:
        model = StoreUser
        fields = ("email", "password1", "password2")
    

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        super(UserRegisterForm, self).set_up_fields()
      

class UserLoginForm(auth_forms.AuthenticationForm, FormFieldsController):
    class_name = "form-control"
    help_text_to_remove = "__all__"
    placeholders = {
        "username": "Enter your email address",
        "password": "Enter your password",
    }
    
    class Meta:
        model = StoreUser
        fields = ('username', 'password')
        
    def __init__(self, *args, **kwargs):
       super(UserLoginForm, self).__init__(*args, **kwargs)
       super(UserLoginForm, self).set_up_fields()


class ChangePasswordForm(auth_forms.PasswordChangeForm, FormFieldsController):
    class_name = "form-control"
    help_text_to_remove = "__all__"
    placeholders = {
        'old_password': "Your old password",
        "new_password1": "Your new password", 
        "new_password2": "Confirm the new password",
    }
    more_validators = {
        "new_password2": [
            validate_password,
            validate_password_contains_uppercase_letter, 
            validate_password_contains_lowercase_letter, 
            validate_password_contains_digit, 
            validate_password_contains_special_symbol,
        ]
    }
    
    
    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        super(ChangePasswordForm, self).set_up_fields()



# Password reset forms
class ResetPasswordForm(auth_forms.PasswordResetForm, FormFieldsController):
     class_name = "form-control"
     placeholders = {
        'email': "Enter your email",
    }
     
     def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)
        super(ResetPasswordForm, self).set_up_fields()



class SetNewPasswordForm(auth_forms.SetPasswordForm, FormFieldsController):
     class_name = "form-control"
     help_text_to_remove = "__all__"
     more_validators = {
        "new_password2": [
            validate_password,
            validate_password_contains_uppercase_letter, 
            validate_password_contains_lowercase_letter, 
            validate_password_contains_digit, 
            validate_password_contains_special_symbol,
        ]
    }
     placeholders = {
        "new_password1": "Your new password", 
        "new_password2": "Confirm the new password",
    }
     
     def __init__(self, *args, **kwargs):
        super(SetNewPasswordForm, self).__init__(*args, **kwargs)
        super(SetNewPasswordForm, self).set_up_fields()