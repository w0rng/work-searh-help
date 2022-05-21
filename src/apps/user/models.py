from apps.helpers.models import UUIDModel
from apps.user.exceptions import NotEnoughMoney
from django.apps import apps
from django.contrib.auth.models import AbstractUser
from django.db import models
from django_lifecycle import LifecycleModelMixin
from django_lifecycle.decorators import hook
from django_lifecycle.hooks import AFTER_CREATE


class UserRole(models.TextChoices):
    employer = "employer", "Работодатель"
    worker = "worker", "Работник"


class User(LifecycleModelMixin, UUIDModel, AbstractUser):
    banned = models.BooleanField("Заблокирован", default=False)
    balance = models.DecimalField("Баланс", max_digits=6, decimal_places=2, default=0)
    role = models.CharField("Роль", max_length=16, choices=UserRole.choices, default=UserRole.worker)

    class Meta(AbstractUser.Meta):
        pass

    @property
    def has_resume(self):
        return self.resume.filter(source=None).exists()

    def get_resume(self):
        return self.resume.filter(source=None).first()

    def update_balance(self, count):
        if count < 0 and self.balance < abs(count):
            raise NotEnoughMoney("Недостаточно средств")
        self.balance += count
        self.save()

    @hook(AFTER_CREATE)
    def create_subscribe(self):
        if not apps.ready:
            return
        from apps.subscription.models import Subscriber

        Subscriber.objects.create(user=self)
