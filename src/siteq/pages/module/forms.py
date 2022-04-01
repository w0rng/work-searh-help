from apps.module.models import Module
from django import forms


class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ("name",)
