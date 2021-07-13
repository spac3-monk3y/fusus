from . import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as _UserAdmin


@admin.register(models.User)
class UserAdmin(_UserAdmin):
    list_display = [
        'email',
        'first_name',
        'phone',
        'organization',
        'last_name',
        'is_staff'
    ]
    search_fields = [
        'email',
        'phone',
        'username',
        'last_name',
        'first_name',
        'organization__name',
    ]
    ordering = ('email',)
    add_fieldsets = (
        (None, {'fields': ('email', 'organization')}),
    ) + _UserAdmin.add_fieldsets
    fieldsets = (
        (None, {'fields': ('organization',)}),
    ) + _UserAdmin.fieldsets

