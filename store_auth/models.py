from django.db import models
from django.contrib.auth import models as auth_models
from store_auth.manager import StoreUserManager



class StoreUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )
    
    is_active = models.BooleanField(
        default=True,
    )
    
    
    USERNAME_FIELD = 'email'
    
    objects = StoreUserManager()
    
    
