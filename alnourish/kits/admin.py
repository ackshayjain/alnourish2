from django.contrib import admin

from .models import Kits


class KitsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'reg_number',
        'date_published',
        'date_modified',
        'is_registered',
    ]


    list_filter = [
        'is_registered',
        'date_published',
        'date_modified',
    ]

admin.site.register(Kits,KitsAdmin)
