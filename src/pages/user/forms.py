from apps.user.models import User, UserRole
from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "role", "email", "password1", "password2")


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "role")
        widgets = {
            "role": forms.Select(choices=UserRole.choices, attrs={"class": "form-control"}),
        }
