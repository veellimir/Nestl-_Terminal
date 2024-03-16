from django.contrib import admin

from .models import *


admin.site.register(Info)

admin.site.site_title = 'Админ-панель склада'
admin.site.site_header = 'Админ-панель склада'
