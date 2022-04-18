from pages.user import forms

from apps.user.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


class RegistrationView(CreateView):
    form_class = forms.RegistrationForm
    success_url = reverse_lazy('pages:login')
    template_name = 'register/../templates/register/register.html'


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = forms.ProfileForm
    success_url = reverse_lazy('pages:home')
    template_name = '../templates/profile.html'

    def get_object(self, *args):
        return self.request.user
