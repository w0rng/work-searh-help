from apps.module.models import Module
from django.db.models import Q
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from siteq.pages.module.forms import ModuleForm
from django.contrib.auth.mixins import AccessMixin


class ModuleView(AccessMixin, ListView):
    form_class = ModuleForm
    template_name = 'pages/module.html'
    model = Module

    def get_queryset(self):
        return super().get_queryset().order_by('pk')
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class UpdateModuleView(CreateView):
    form_class = ModuleForm
    success_url = reverse_lazy('pages:modules')
    template_name = 'pages/module.html'

    def post(self, request, *args, **kwargs):
        for pk in request.POST.keys():
            ids = [i for i in request.POST.keys() if i.isdigit()]
            Module.objects.filter(pk__in=ids).update(enable=True)
            Module.objects.filter(~Q(pk__in=ids)).update(enable=False)
        return HttpResponseRedirect(self.success_url)

    def get(self, request):
        return HttpResponseRedirect(self.success_url)
