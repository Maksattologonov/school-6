from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import UserChangeForm
from .models import CustomUser


class UserCreateAdmin(BaseUserAdmin):
    list_display = ('username', )
    list_filter = ('username',)
    search_fields = ('username', 'role', 'name')


class UserChangeAdmin(UserChangeForm):
    list_display = ('username', )
    list_filter = ('username',)
    search_fields = ('username', 'role', 'name')


admin.site.register(CustomUser, UserCreateAdmin)
admin.site.unregister(Group)
