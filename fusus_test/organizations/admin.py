from . import models
from django.contrib import admin

extra_description_fieldset = (
    'Extra info', {
        'fields': ['description'],
        'classes': ['collapse']
    }
)


@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'created_at',
    ]
    search_fields = [
        'name',
        'phone',
        'address',
    ]
    list_filter = ['created_at']
    fieldsets = [
        (
            None,
            {
                'fields': [
                    'name',
                    'phone',
                    'address',
                ]
            }
        ),
        extra_description_fieldset
    ]
