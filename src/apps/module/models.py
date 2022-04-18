import requests
from apps.helpers.models import UUIDModel, enum_max_length
from apps.module.exceptions import NotHaveSubscribe
from apps.user.models import User
from django.db import models
from django_lifecycle import AFTER_SAVE, BEFORE_CREATE, LifecycleModel, hook


class ModuleType(models.TextChoices):
    FILTER = "filter", "Фильтр"
    DATA_SOURCE = "source", "Источник данных"


class Module(UUIDModel, LifecycleModel):
    name = models.CharField("Название", max_length=50, unique=True)
    type = models.CharField("Тип", max_length=enum_max_length(ModuleType), choices=ModuleType.choices)
    description = models.TextField("Описание")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    endpoint = models.URLField("Эндпоинт")
    for_all_users = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @hook(BEFORE_CREATE)
    def check_user(self):
        if self.author.subscriber.subscription.level == 0:
            raise NotHaveSubscribe()

    @hook(AFTER_SAVE)
    def if_for_all_users(self):
        if not self.for_all_users:
            return

        users = User.objects.filter(pk__in=ConfigModule.objects.filter(module=self).values_list("user", flat=True))
        configs = [ConfigModule(user=user, module=self, enabled=True) for user in users]
        ConfigModule.objects.bulk_create(configs)

    def load(self, user: User):
        response = requests.get(f"{self.endpoint}/vacancies", params={"id": self.id})
        if not response.ok:
            return


class ConfigModule(LifecycleModel, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    module = models.ForeignKey(Module, on_delete=models.CASCADE, verbose_name="Модуль")
    enabled = models.BooleanField("Включен", default=True)

    @hook(BEFORE_CREATE)
    def check_user(self):
        if self.user.subscriber.subscription.level == 0:
            raise NotHaveSubscribe()
        if self.user.subscriber.subscription.level == 1 and self.user != self.module.author:
            raise NotHaveSubscribe()

    class Meta:
        unique_together = ["user", "module"]
