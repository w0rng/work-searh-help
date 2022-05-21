from apps.enemy.models import Enemy
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Resume(Enemy):
    fio = models.CharField(max_length=100, verbose_name="ФИО", blank=True, null=True, default=None)
    user = models.ForeignKey(User, models.SET_NULL, null=True, verbose_name="Пользователь", related_name="resume")

    def __str__(self):
        return f"{self.user} {self.name}"
