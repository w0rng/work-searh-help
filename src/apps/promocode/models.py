from hashlib import md5

from apps.promocode.manager import PromocodeManager
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.db import models
from django_lifecycle import AFTER_CREATE, BEFORE_CREATE, LifecycleModel, hook
from apps.helpers.models import CreatedModel, PriceField

User = get_user_model()


class Promocode(LifecycleModel, models.Model):
    code = models.CharField('Промокод', max_length=32, unique=True)
    max_activations = models.PositiveSmallIntegerField('Максимум активаций', default=1)
    count_activations = models.PositiveSmallIntegerField('Всего активаций', default=0)
    price = PriceField('Цена')

    objects = PromocodeManager()

    class Meta:
        verbose_name = 'Промокод'
        verbose_name_plural = 'Промокоды'

    def __str__(self) -> str:
        return f'md5-{self.code[:4]}'

    @hook(BEFORE_CREATE)
    def hash_code(self):
        hash = md5(self.code.encode('utf-8'))
        self.code = hash.hexdigest()

    def activate(self):
        if self.count_activations >= self.max_activations:
            raise PermissionDenied('Достигнуто максимальное число активаций')
        self.count_activations += 1
        self.save()

class Activation(LifecycleModel, CreatedModel):
    user = models.ForeignKey(User, models.CASCADE)
    promocode = models.ForeignKey(Promocode, models.CASCADE)

    class Meta:
        verbose_name = 'Активация'
        verbose_name_plural = 'Активации'
        unique_together = ('user', 'promocode')

    @hook(AFTER_CREATE)
    def activate(self):
        self.promocode.activate()
        self.user.balance += self.promocode.price
        self.user.save()
