from apps.enemy.models import Tag
from apps.vacancy.models import Vacancy
from django import forms
from django.contrib.admin import widgets


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        exclude = ["user", "source"]
