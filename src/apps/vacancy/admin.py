from apps.vacancy.models import Vacancy
from django.contrib import admin


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ("name",)
    filter_horizontal = ("tags", "tags")
