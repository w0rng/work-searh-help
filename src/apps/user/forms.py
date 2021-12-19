from django import forms
from apps.user.models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
