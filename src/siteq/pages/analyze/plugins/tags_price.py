from apps.resume.models import Tag
from django.db.models.aggregates import Avg
from siteq.pages.analyze.plugins.base import BaseAnalyzer


class Tags_PriceAnalyzer(BaseAnalyzer):
    name = 'Зарплаты по тегам'
    level = 2
    description = 'Средняя зарплата по каждому тегу'

    def get_queryset(self, request):
        return Tag.objects.all().annotate(count=Avg('vacancies__price')).filter(count__gt=2)
