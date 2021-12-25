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
            return Vacancy.objects.all()
        queryset = self.model.objects.all()
        for filter in filters:
            print(filter, flush=True)
            queryset = filter().do(self.request, queryset)
        return queryset
