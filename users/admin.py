from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name', )}
    list_display = ('category_name', )
    list_display_links = ('category_name', )


class ProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ('name', 'profile_admin_image', 'is_public')
    list_display_links = ('name', )

    list_editable = ('is_public', )

    fields = (
        'name',
        'slug',
        'profile_admin_image',
        'collected',
        'transported',
        'discharge',
        'shipment',
        'others',
        'is_public',
        'employee_category',
    )
    readonly_fields = ('profile_admin_image', 'time_employment')

    def profile_admin_image(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="150">')

    profile_admin_image.short_description = 'Изображение профиля'


admin.site.register(Profile, ProfileAdmin)
admin.site.register(CategoryEmployee, CategoryAdmin)
