from threading import Thread

import requests
from apps.enemy.models import Enemy
from apps.user.models import User
from django.db import models
from django.db.models import Q
from django_lifecycle import hook
from django_lifecycle.hooks import AFTER_CREATE


class Vacancy(Enemy):
    description = models.TextField("Описание")
    user = models.ForeignKey(User, models.SET_NULL, null=True, verbose_name="Пользователь", related_name="vacancy")

    @hook(AFTER_CREATE)
    def export(self):
        if self.source is not None:
            return
        from api.v1.vacancy.serializers import VacancySerializer
        from apps.module.models import ConfigModule, Module, ModuleType

        def run():
            modules = Module.objects.filter(
                pk__in=ConfigModule.objects.filter(user=self.user, enabled=True)
                .values_list("module", flat=True)
                .filter(module__type=ModuleType.EXPORTER)
                .filter(Q(module__role__isnull=True) | Q(module__role=self.user.role))
            )
            for module in modules:
                try:
                    requests.post(module.endpoint, json=VacancySerializer(self).data)
                except Exception as e:
                    pass

        Thread(target=run).start()
