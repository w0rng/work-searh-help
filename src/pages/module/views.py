from apps.module.models import ConfigModule, Module
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Q
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from pages.module.forms import ModuleForm


class ModuleView(LoginRequiredMixin, ListView):
    form_class = ModuleForm
    template_name = "pages/module.html"
    model = Module

    def get_queryset(self):
        user = self.request.user
        if not user or not user.is_authenticated:
            queryset = Module.objects.none()
        elif user.subscriber.subscription.level == 0:
            queryset = Module.objects.none()
        elif user.subscriber.subscription.level == 1:
            queryset = Module.objects.filter(author=user)
        else:
            queryset = Module.objects.filter(Q(author=user) | Q(public=True))
        queryset = queryset.annotate(
            enabled=Count(
                "configmodule",
                filter=Q(configmodule__enabled=True),
            )
        ).order_by("-enabled")
        return queryset


class UpdateModuleView(CreateView):
    form_class = ModuleForm
    success_url = reverse_lazy("pages:modules")
    template_name = "pages/module.html"

    def post(self, request, *args, **kwargs):
        module_id = request.POST.get("module")
        if not module_id:
            return HttpResponseRedirect(self.success_url)
        module = Module.objects.get(pk=module_id)
        if not module:
            return HttpResponseRedirect(self.success_url)
        if request.user.subscriber.subscription.level == 0:
            return HttpResponseRedirect(self.success_url)
        if request.user.subscriber.subscription.level == 1:
            if module.author != request.user:
                return HttpResponseRedirect(self.success_url)
        config, created = ConfigModule.objects.get_or_create(module=module, user=request.user)
        config.enabled = created or not config.enabled
        config.save()

        return HttpResponseRedirect(self.success_url)

    def get(self, request):
        return HttpResponseRedirect(self.success_url)
