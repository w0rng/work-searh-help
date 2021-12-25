from django.contrib import admin
from apps.module.models import Module


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'enable')
