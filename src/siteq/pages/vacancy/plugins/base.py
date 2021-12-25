from django.db.models.query import QuerySet
from apps.vacancy.models import Vacancy
from apps.module.models import ModuleClass


class BaseFilter(ModuleClass):
    def _filter(self, request, queryset: QuerySet[Vacancy]):
        pass

    def do(self, request, queryset: QuerySet[Vacancy]):
        queryset = queryset.distinct()
        if not self.module.enable:
            return queryset
        if self.level > request.user.subscriber.subscription.level:
            return queryset
        return self._filter(request, queryset)
