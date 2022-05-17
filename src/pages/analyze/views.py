from apps.resume.models import Tag
from django.db.models.aggregates import Count
from django.views.generic import TemplateView


class EditorChartView(TemplateView):
    template_name = "pages/chart.html"

    def get_context_data(self, **kwargs):
        name = self.request.GET.get("name", "")
        if not name:
            return
        context = super().get_context_data(**kwargs)
        # context['qs'] = analyzers[name].get_queryset(self.request)
        # context['description'] = analyzers[name].description
        return context
