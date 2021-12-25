from django.db.models.query import QuerySet
from siteq.pages.vacancy import forms

from apps.vacancy.models import Vacancy
from django.views.generic import ListView
from siteq.pages.vacancy.plugins.load import filters


class VacancyView(ListView):
    model = Vacancy
    form_class = forms.VacancyForm
    template_name = 'pages/vacancy.html'
    paginate_by = 21

    def get_queryset(self):
        if 'all' in self.request.path:
            return super().get_queryset()
        queryset = super().get_queryset()
        filtered = []
        for filter in filters:
            filtered.append((filter.do(self.request, queryset), filter.model.level))

        vacancies = []
        for vacancy in queryset:
            score = sum([f[1]+1 for f in filtered if vacancy in f[0]])
            vacancies.append((vacancy, score))
        
        vacancies.sort(key=lambda x: x[1], reverse=True)
        vacancies = [v[0] for v in vacancies if v[1] >= vacancies[0][1]*0.7]

        return vacancies
