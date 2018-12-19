from django.contrib import admin
from .models import Icon


class IconAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Icon, IconAdmin)
