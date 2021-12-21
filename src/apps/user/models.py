from django.contrib.auth.models import AbstractUser
from django_lifecycle.decorators import hook
from django_lifecycle.hooks import AFTER_CREATE
from apps.user.exceptions import NotEnoughMoney
from django_lifecycle import LifecycleModelMixin
from apps.helpers.models import UUIDModel
from django.db import models


class UserRole(models.TextChoices):
    default = 'dflt', 'Обычный пользователь'
    subscription = 'subs', 'Подписчик'
    advertiser = 'adve', 'Рекламодатель'


class User(LifecycleModelMixin, UUIDModel, AbstractUser):
    banned = models.BooleanField('Заблокирован', default=False)
    balance = models.DecimalField('Баланс', max_digits=6, decimal_places=2, default=0)
    role = models.CharField('Роль', max_length=4, choices=UserRole.choices, default=UserRole.default)

    class Meta(AbstractUser.Meta):
        pass

    def update_balance(self, count):
        if count < 0 and self.balance < abs(count):
            raise NotEnoughMoney('Недостаточно средств')
        self.balance += count
        self.save()

    @hook(AFTER_CREATE)
    def create_subscribe(self):
        from apps.subscription.models import Subscriber
        Subscriber.objects.create(user=self)
