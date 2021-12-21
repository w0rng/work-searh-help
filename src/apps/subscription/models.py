from django.contrib.auth import get_user_model
from django.db import models
from apps.helpers.models import UUIDModel, PriceField
from django_lifecycle import LifecycleModelMixin, hook, BEFORE_UPDATE


User = get_user_model()

class Subscription(UUIDModel):
    name = models.CharField('Название', max_length=50, unique=True)
    price = PriceField('Цена')
    level = models.PositiveSmallIntegerField('Уровень', default=0)

    @classmethod
    def get_default(cls):
        return cls.objects.get_or_create(name='Free', price=0, level=0)[0]

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return self.name


class Subscriber(LifecycleModelMixin, UUIDModel):
    user = models.OneToOneField(User, verbose_name='Подписчик', on_delete=models.CASCADE, related_name='subscriber')
    subscription = models.OneToOneField(Subscription, verbose_name='Подписка', on_delete=models.SET_DEFAULT, default=Subscription.get_default)

    class Meta:
        unique_together = ('user', 'subscription')

    @hook(BEFORE_UPDATE, when='subscription')
    def subscribe(self):
        self.user.update_balance(-self.subscription.price)
