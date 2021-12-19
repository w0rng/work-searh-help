from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from pages.promocode.forms import PromocodeForm
from apps.promocode.models import Promocode
from django.contrib import messages


class PromocodeView(CreateView):
    form_class = PromocodeForm
    success_url = reverse_lazy('pages:promocode')
    template_name = 'pages/promocode.html'

    def post(self, request, *args, **kwargs):
        code = request.POST['code']
        try:
            self.object = Promocode.objects.get(code=code)
            request.user.balance += self.object.price
            request.user.save()
            self.object.activate()
            messages.success(request, 'Промокод успешно активирован')
        except ObjectDoesNotExist:
            messages.error(request, 'Промокод не найден')
        except PermissionDenied:
            messages.warning(request, 'Количество активаций промокода закончилось')

        return HttpResponseRedirect(self.success_url)
