from apps.enemy.models import Enemy
from apps.user.models import User
from django.db import models


class Vacancy(Enemy):
    description = models.TextField("Описание")
    user = models.ForeignKey(User, models.SET_NULL, null=True, verbose_name="Пользователь", related_name="vacancy")
