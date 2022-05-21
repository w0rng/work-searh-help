from apps.module.models import ConfigModule
from apps.resume.models import Resume
from apps.user.models import UserRole
from connectors.filters import FilterResumes
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from pages.resume.forms import ResumeForm
from pages.vacancy.forms import VacancyForm


class ResumeView(LoginRequiredMixin, CreateView, UpdateView, ListView):
    success_url = reverse_lazy("pages:vacancies")
    template_name = "pages/resume.html"
    paginate_by = 21

    def get_form_class(self):
        user = self.request.user
        if user.role == UserRole.employer and user.vacancy.count() == 0:
            return VacancyForm
        return ResumeForm

    def get_queryset(self):
        user = self.request.user
        return FilterResumes(user).filter()

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_object(self, *args):
        if self.request.user.has_resume:
            return self.request.user.get_resume()
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count_pages"] = range(1, min(context["page_obj"].paginator.num_pages, 10) + 1)
        context["random_colors"] = ["primary", "secondary", "success", "danger", "warning", "info", "dark"]
        return context
