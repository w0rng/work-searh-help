from django.db.models.query import QuerySet
from siteq.pages.vacancy.plugins.base import BaseFilter
from apps.vacancy.models import Vacancy


class TagsFilter(BaseFilter):
    name = 'Фильтр по тегам'
    level = 1

    def _filter(self, request, queryset: QuerySet[Vacancy]):
        tags = [t for t in request.user.resume.tags.all() if t.vacancies.count() > 0]
        return queryset.filter(tags__in=tags)
