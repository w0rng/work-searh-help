from django.db.models.query import QuerySet
from siteq.pages.vacancy.plugins.base import BaseFilter
from apps.vacancy.models import Vacancy
from apps.resume.models import Resume


class TagsFilter(BaseFilter):
    name = 'Фильтр по тегам'
    level = 1

    def _filter(self, request, queryset: QuerySet[Vacancy]):
        tags = Resume.objects.filter(user=request.user).values_list('tags', flat=True)
        return queryset.filter(tags__in=tags.distinct())
