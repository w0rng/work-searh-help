from django.contrib import admin
from apps.resume.models import Tag, Resume


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Resume)
class ActivationAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'user', 'price')
