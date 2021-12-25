from apps.subscription.models import Subscriber, Subscription
from apps.user.exceptions import NotEnoughMoney
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from siteq.pages.subscription import forms
from apps.vacancy.models import BaseFilter
from siteq.pages.vacancy.plugins.load import filters


class SubscriptionView(ListView):
    form_class = forms.SubscriptionForm
    template_name = 'pages/subscription.html'
    model = Subscription

    def get_queryset(self):
        return super().get_queryset().order_by('level')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filters"] = BaseFilter.objects.all()
        return context


class SubscriptionCreateView(CreateView):
    form_class = forms.SubscriptionForm
    template_name = 'pages/subscription.html'
    success_url = reverse_lazy('pages:subscriptions')
    model = Subscription

    def post(self, request, *args, **kwargs):
        sub = request.POST.get('sub')
        if not sub:
            return HttpResponseRedirect(self.success_url)
        sub = self.model.objects.filter(pk=sub)
        if not sub:
            messages.error(request, 'Подписка не найдена')

        sub = sub.first()
        try:
            request.user.update_balance(-sub.price)
            Subscriber.objects.filter(user=request.user).update(subscription=sub)
            messages.success(request, 'Ваша подписка успешно обновлена')
        except NotEnoughMoney:
            messages.warning(request, 'У вас недостаточно средств')
        return HttpResponseRedirect(self.success_url)
