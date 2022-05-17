from apps.resume.models import Resume
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from pages.resume import forms


class ResumeView(LoginRequiredMixin, CreateView, UpdateView, ListView):
    form_class = forms.ResumeForm
    success_url = reverse_lazy("pages:vacancies")
    template_name = "pages/resume.html"

    def get_queryset(self):
        return Resume.objects.all()

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_object(self, *args):
        if hasattr(self.request.user, "resume"):
            return self.request.user.resume
        return None
