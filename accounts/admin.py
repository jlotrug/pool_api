from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "first_name",
        "last_name",
        "wins",
        "is_staff",
    ]

    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("wins",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None,{"fields": ("wins",)}),)

admin.site.register(CustomUser, CustomUserAdmin)