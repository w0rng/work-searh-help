from django import forms
from apps.promocode.models import Promocode


class PromocodeForm(forms.ModelForm):
    class Meta:
        model = Promocode
        fields = ('code', )
