from apps.user.models import UserRole
from apps.vacancy.models import Vacancy
from connectors.filters import FilterVacancies
from django.contrib.auth.mixins import LoginRequiredMixin
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
        return FilterVacancies(user).filter()

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count_pages"] = range(1, min(context["page_obj"].paginator.num_pages, 10) + 1)
        return context