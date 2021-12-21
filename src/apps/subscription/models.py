from django.contrib.auth import get_user_model
from django.db import models
from apps.helpers.models import UUIDModel, PriceField
from django_lifecycle import LifecycleModelMixin, hook, BEFORE_CREATE


User = get_user_model()

class Subscription(UUIDModel):
    name = models.CharField('Название', max_length=50, unique=True)
    price = PriceField('Цена')

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return self.name


class Subscriber(LifecycleModelMixin, UUIDModel):
    user = models.ForeignKey(User, verbose_name='Подписчик', on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, verbose_name='Подписка', on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = ('user', 'subscription')

    @hook(BEFORE_CREATE)
    def subscribe(self):
        self.user.update_balance(-self.subscription.price)
