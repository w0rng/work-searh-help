from django.contrib import admin
from apps.vacancy.models import Vacancy, BaseFilter


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(BaseFilter)
class BaseFilterAdmin(admin.ModelAdmin):
    list_display = ('name', 'enable')
