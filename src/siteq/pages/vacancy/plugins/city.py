from django.db.models.query import QuerySet
from siteq.pages.vacancy.plugins.base import BaseFilter
from apps.vacancy.models import Vacancy


class CityFilter(BaseFilter):
    name = 'Фильтр по городу'
    level = 0
    show = True

    def _filter(self, request, queryset: QuerySet[Vacancy]):
        return queryset.filter(city=request.user.resume.city)
