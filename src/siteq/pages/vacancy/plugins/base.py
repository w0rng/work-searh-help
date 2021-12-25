from django.db.models.query import QuerySet
from apps.vacancy.models import BaseFilter as Filter, Vacancy
from abc import ABC

class BaseFilter(ABC):
    name: str
    level: int

    def __init__(self):
        self.model = Filter.objects.get_or_create(name=self.name, level=self.level)[0]

    def _filter(self, request, queryset: QuerySet[Vacancy]):
        pass

    def do(self, request, queryset: QuerySet[Vacancy]):
        queryset = queryset.distinct()
        if not self.model.enable:
            return queryset
        if self.level > request.user.subscriber.subscription.level:
            return queryset
        return self._filter(request, queryset)
