from django.db.models.query import QuerySet
from siteq.pages.vacancy.plugins.base import BaseFilter
from apps.vacancy.models import Vacancy
from decimal import Decimal
from random import choices, seed, randint



class NeuralFilter(BaseFilter):
    name = 'Хитрайя нейронная сеть'
    level = 2

    def _filter(self, request, queryset: QuerySet[Vacancy]):
        seed(request.user)
        ids = queryset.values_list('pk', flat=True)
        ids = choices(ids, k=randint(len(ids)//2, len(ids)))
        return queryset.filter(id__in=ids)
