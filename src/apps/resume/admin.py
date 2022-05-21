from apps.enemy.models import Tag
from apps.resume.models import Resume
from django.contrib import admin


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Resume)
class ActivationAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "price")
    filter_horizontal = ["tags"]
