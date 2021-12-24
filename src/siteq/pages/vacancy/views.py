from siteq.pages.vacancy import forms

from apps.resume.models import Resume
from apps.vacancy.models import Vacancy
from django.views.generic import ListView


class VacancyView(ListView):
    model = Vacancy
    form_class = forms.VacancyForm
    template_name = 'pages/vacancy.html'

    def get_queryset(self):
        if 'all' in self.request.path:
            return Vacancy.objects.all()
        tags = Resume.objects.filter(user=self.request.user).values_list('tags', flat=True)
        return Vacancy.objects.filter(tags__in=tags.distinct()).order_by('-price')
