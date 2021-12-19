from django.contrib.auth.models import AbstractUser
from django_lifecycle import LifecycleModelMixin
from helpers.models import UUIDModel
from django.db import models


class User(LifecycleModelMixin, UUIDModel, AbstractUser):
    banned = models.BooleanField('Заблокирован', default=False)

    class Meta(AbstractUser.Meta):
        pass
