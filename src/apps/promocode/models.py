from hashlib import md5
from django.core.exceptions import PermissionDenied
from django.db import models
from django_lifecycle import LifecycleModel, hook, BEFORE_CREATE
from apps.promocode.manager import PromocodeManager



class Promocode(LifecycleModel, models.Model):
    code = models.CharField('Промокод', max_length=32, unique=True)
    max_activations = models.PositiveSmallIntegerField('Максимум активаций', default=1)
    count_activations = models.PositiveSmallIntegerField('Всего активаций', default=0)
    price = models.DecimalField('Цена', max_digits=5, decimal_places=2)

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
