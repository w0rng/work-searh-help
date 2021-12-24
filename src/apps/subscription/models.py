from apps.helpers.models import UUIDModel
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django_lifecycle import BEFORE_UPDATE, LifecycleModelMixin, hook

User = get_user_model()

class Subscription(UUIDModel):
    name = models.CharField('Название', max_length=50, unique=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0)]
    )
    level = models.PositiveSmallIntegerField('Уровень')

    @classmethod
    def get_default(cls):
        return cls.objects.get_or_create(name='Free', price=0, level=0)[0]

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return self.name


class Subscriber(LifecycleModelMixin, UUIDModel):
    user = models.OneToOneField(User, verbose_name='Подписчик', on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, verbose_name='Подписка', on_delete=models.SET_DEFAULT, default=Subscription.get_default)

    class Meta:
        unique_together = ('user', 'subscription')
