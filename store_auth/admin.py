from django.contrib import admin
from store_auth.models import StoreUser

@admin.register(StoreUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email',)
