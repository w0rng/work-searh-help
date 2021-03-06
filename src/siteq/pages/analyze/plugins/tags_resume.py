from apps.resume.models import Tag
from django.db.models.aggregates import Count
from siteq.pages.analyze.plugins.base import BaseAnalyzer


class Tags_ResumeAnalyzer(BaseAnalyzer):
    name = 'Количество резюме по тегам'
    level = 1
    description = 'Количество резюме с разными тегами'

    def get_queryset(self, request):
        return Tag.objects.all().annotate(count=Count('resumes')).filter(count__gt=2)
