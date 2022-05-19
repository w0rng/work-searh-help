from apps.module.models import ConfigModule, Module
from apps.user.models import UserRole
from apps.vacancy.models import Vacancy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from pages.vacancy import forms


class VacancyView(LoginRequiredMixin, CreateView, ListView):
    model = Vacancy
    form_class = forms.VacancyForm
    template_name = "pages/vacancy.html"
    success_url = reverse_lazy("pages:vacancies")
    paginate_by = 21

    def get_queryset(self):
        user = self.request.user
        if user.role == UserRole.employer:
            return Vacancy.objects.filter(user=user)
        return Vacancy.objects.filter(
            Q(source__id__in=ConfigModule.objects.filter(user=user, enabled=True).values_list("module", flat=True))
            | Q(source__isnull=True)
        )

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return super().post(request, *args, **kwargs)
