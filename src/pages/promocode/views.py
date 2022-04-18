from apps.promocode.models import Activation, Promocode
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.db import IntegrityError
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from pages.promocode.forms import PromocodeForm
from django.contrib.auth.mixins import LoginRequiredMixin


class PromocodeView(LoginRequiredMixin, CreateView):
    form_class = PromocodeForm
    success_url = reverse_lazy('pages:promocode')
    template_name = 'pages/../templates/pages/promocode.html'

    def post(self, request, *args, **kwargs):
        code = request.POST['code']
        try:
            self.object = Promocode.objects.get(code=code)
            Activation.objects.create(user=request.user, promocode=self.object)
            messages.success(request, 'Промокод успешно активирован')
        except ObjectDoesNotExist:
            messages.error(request, 'Промокод не найден')
        except PermissionDenied:
            messages.warning(request, 'Количество активаций промокода закончилось')
        except IntegrityError:
            messages.error(request, 'Вы уже активировали этот промокод')

        return HttpResponseRedirect(self.success_url)
