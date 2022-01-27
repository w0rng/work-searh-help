from apps.resume.models import Tag
from django.db.models.aggregates import Count
from siteq.pages.analyze.plugins.base import BaseAnalyzer


class TagsAnalyzer(BaseAnalyzer):
    name = 'Анализ тегов'
    level = 1
    description = 'Количество вакансий с разными тегами'

    def get_queryset(self, request):
        return Tag.objects.all().annotate(count=Count('vacancies')).filter(count__gt=2)
