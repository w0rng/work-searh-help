from django import forms
from apps.module.models import Module


class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ('name', 'enable',)
