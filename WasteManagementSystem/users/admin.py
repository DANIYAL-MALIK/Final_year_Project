from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreateForm
# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = User
    add_form = UserCreateForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (('Management'), {'fields': ('isManager',)}))


admin.site.register(User, CustomUserAdmin)