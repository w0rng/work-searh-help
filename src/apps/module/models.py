from django.db import models
from django.core.validators import MinValueValidator
from abc import ABC


class ModuleType(models.TextChoices):
    FILTER = 'f', 'Фильтр'
    SITE = 's', 'Фичи'


class Module(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)
    level = models.PositiveIntegerField('Уровень', default=0, validators=[
        MinValueValidator(0),
    ])
    enable = models.BooleanField('Включен', default=True)
    show = models.BooleanField('Отображать', default=True)
    type = models.CharField('Тип', max_length=1, choices=ModuleType.choices)


class ModuleClass(ABC):
    name: str
    level: int
    show: bool
    type = ModuleType.FILTER

    def __init__(self):
        self.module, created = Module.objects.get_or_create(name=self.name)
        if created:
            self.module.level = self.level
            self.module.show = self.show
            self.module.type = self.type
            self.module.save()
