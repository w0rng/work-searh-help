from apps.enemy.models import Enemy
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Resume(Enemy):
    user = models.OneToOneField(User, models.SET_NULL, verbose_name="Пользователь", related_name="resume", null=True)

    def __str__(self):
        return f"{self.user} {self.name}"
