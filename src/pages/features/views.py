from django.views.generic.base import TemplateView
from random import randint


class HomePage(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['random_year'] = randint(1900, 2000)
        return context