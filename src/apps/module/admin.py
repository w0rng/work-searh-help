from apps.module.models import ConfigModule, Module
from django.contrib import admin


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "author", "enabled_count", "all_count")

    def enabled_count(self, obj: Module):
        return obj.configmodule_set.filter(enabled=True).count()

    def all_count(self, obj: Module):
        return obj.configmodule_set.all().count()


@admin.register(ConfigModule)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ("module", "user", "enabled")
