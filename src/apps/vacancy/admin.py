from django.contrib import admin
from apps.vacancy.models import Vacancy


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('name',)
