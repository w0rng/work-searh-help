from apps.vacancy.models import Vacancy
from django import forms


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        exclude = ["user", "source"]
