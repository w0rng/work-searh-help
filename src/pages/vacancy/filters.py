from django_filters import FilterSet
from apps.vacancy.models import Vacancy


class VacancyFilter(FilterSet):
    class Meta:
        model = Vacancy
        fields = ('price', 'tags', 'city', 'remote')
