from django.views.generic import ListView
from pages.vacancy import forms
from apps.vacancy.models import Vacancy
from apps.resume.models import Resume


class VacancyView(ListView):
    model = Vacancy
    form_class = forms.VacancyForm
    template_name = 'pages/vacancy.html'

    def get_queryset(self):
        #return Vacancy.objects.filter(tags__in=self.request.user.resume.tags, allowed=True)
        tags = Resume.objects.filter(user=self.request.user).values_list('tags', flat=True)
        print(Vacancy.objects.filter(tags__in=tags.distinct()), flush=True)
        return Vacancy.objects.filter(tags__in=tags.distinct())
