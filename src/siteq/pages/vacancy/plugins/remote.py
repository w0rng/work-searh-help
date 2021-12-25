from django.db.models.query import QuerySet
from siteq.pages.vacancy.plugins.base import BaseFilter
from apps.vacancy.models import Vacancy


class RemoteFilter(BaseFilter):
    name = 'Удаленная работа'
    level = 0
    show = True

    def _filter(self, request, queryset: QuerySet[Vacancy]):
        return queryset.filter(remote=request.user.resume.remote)
