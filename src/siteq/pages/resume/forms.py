from django import forms
from apps.resume.models import Resume


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        exclude = ['user']
