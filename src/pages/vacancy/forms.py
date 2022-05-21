from apps.enemy.models import Tag
from apps.vacancy.models import Vacancy
from django import forms
from easy_select2 import Select2Multiple


class VacancyForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=Select2Multiple(
            select2attrs={
                "width": "100%",
                "height": "100%",
            }
        ),
    )

    class Meta:
        model = Vacancy
        exclude = ["user", "source", "source_pk"]
