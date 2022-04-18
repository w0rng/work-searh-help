from apps.module.models import ConfigModule
from apps.vacancy.models import Vacancy
from apps.vacancy.services.load_from_hh import Loader
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from pages.vacancy import forms


class VacancyView(LoginRequiredMixin, ListView):
    model = Vacancy
    form_class = forms.VacancyForm
    template_name = "pages/../templates/pages/vacancy.html"
    paginate_by = 21

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["filter"] = VacancyFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def dispatch(self, request, *args, **kwargs):
        if "all" in self.request.path:
            return ListView.dispatch(self, request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        if self.request.user.resume:
            Loader.load(self.request.user.resume)
        if "all" in self.request.path:
            return super().get_queryset()
        queryset = super().get_queryset()
        filtered = []
        # for filter in filters:
        #     filtered.append((filter.do(self.request, queryset), filter.module.level))

        vacancies = []
        for vacancy in queryset:
            score = sum([f[1] + 1 for f in filtered if vacancy in f[0]])
            vacancies.append((vacancy, score))

        vacancies.sort(key=lambda x: x[1], reverse=True)
        vacancies = [v[0] for v in vacancies if v[1] >= vacancies[0][1] * 0.7]

        return vacancies
