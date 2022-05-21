from apps.enemy.models import Tag
from apps.resume.models import Resume
from django import forms
from easy_select2 import Select2Multiple


class ResumeForm(forms.ModelForm):
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
        model = Resume
        exclude = ["user", "source", "source_pk"]
