from apps.helpers.models import CreatedModel, UUIDModel
from apps.module.models import Module
from django.core.validators import MinValueValidator
from django.db import models
from django_lifecycle import LifecycleModelMixin


class Tag(models.Model):
    name = models.CharField("Название", unique=True, primary_key=True, max_length=32)

    def __str__(self):
        return self.name


class Enemy(LifecycleModelMixin, UUIDModel, CreatedModel):
    name = models.CharField("Название", max_length=255)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    tags = models.ManyToManyField(Tag, related_name="resumes", verbose_name="Навыки")
    city = models.CharField("Город", max_length=50, null=True)
    remote = models.BooleanField("Удаленная работа", default=False)
    source = models.ForeignKey(Module, models.SET_NULL, null=True, verbose_name="Источник")
    source_pk = models.CharField("Первичный ключ из источника", max_length=255, null=True)
