from apps.module.models import ConfigModule
from apps.resume.models import Resume
from apps.user.models import UserRole
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from pages.resume.forms import ResumeForm
from pages.vacancy.forms import VacancyForm


class ResumeView(LoginRequiredMixin, CreateView, UpdateView, ListView):
    success_url = reverse_lazy("pages:vacancies")
    template_name = "pages/resume.html"

    def get_form_class(self):
        user = self.request.user
        if user.role == UserRole.employer and user.vacancy.count() == 0:
            return VacancyForm
        return ResumeForm

    def get_queryset(self):
        user = self.request.user
        return Resume.objects.filter(
            Q(source__id__in=ConfigModule.objects.filter(user=user, enabled=True).values_list("module", flat=True))
            | Q(source__isnull=True)
        )

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_object(self, *args):
        if hasattr(self.request.user, "resume"):
            return self.request.user.resume
        return None
