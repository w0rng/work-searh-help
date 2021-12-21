from django import forms
from apps.vacancy.models import Vacancy



class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ('name', 'price', 'tags')
