from apps.helpers.models import UUIDModel, enum_max_length
from apps.module.exceptions import NotHaveSubscribe
from apps.user.models import User
from django.db import models
from django_lifecycle import BEFORE_CREATE, LifecycleModel, hook


class ModuleType(models.TextChoices):
    FILTER = "filter", "Фильтр"
    DATA_SOURCE = "source", "Источник данных"


class Module(UUIDModel, LifecycleModel):
    name = models.CharField("Название", max_length=50, unique=True)
    type = models.CharField("Тип", max_length=enum_max_length(ModuleType), choices=ModuleType.choices)
    description = models.TextField("Описание")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    endpoint = models.URLField("Эндпоинт")

    def __str__(self):
        return self.name

    @hook(BEFORE_CREATE)
    def check_user(self):
        if self.author.subscriber.subscription.level == 0:
            raise NotHaveSubscribe()


class ConfigModule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    module = models.ForeignKey(Module, on_delete=models.CASCADE, verbose_name="Модуль")
    enabled = models.BooleanField("Включен", default=True)

    class Meta:
        unique_together = ["user", "module"]
