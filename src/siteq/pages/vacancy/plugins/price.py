from django.db.models.query import QuerySet
from siteq.pages.vacancy.plugins.base import BaseFilter
from apps.vacancy.models import Vacancy
from decimal import Decimal



class PriceFilter(BaseFilter):
    name = 'Фильтр по цене'
    level = 0

    def _filter(self, request, queryset: QuerySet[Vacancy]):
        resume = request.user.resume
        return queryset.filter(
            price__gte=resume.price*Decimal(0.8),
            price__lte=resume.price*Decimal(1.4)
        ).order_by('-price')
