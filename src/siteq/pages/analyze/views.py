from django.db.models.aggregates import Count
from django.views.generic import TemplateView
from apps.resume.models import Tag


class EditorChartView(TemplateView):
    template_name = 'pages/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Tag.objects.annotate(count=Count('vacancies')).filter(count__gt=2)
        return context
