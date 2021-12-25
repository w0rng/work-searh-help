from django.db import models
from django.core.validators import MinValueValidator
from abc import ABC


class Module(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)
    level = models.PositiveIntegerField('Уровень', default=0, validators=[
        MinValueValidator(0),
    ])
    enable = models.BooleanField('Включен', default=True)
    show = models.BooleanField('Отображать', default=True)


class ModuleClass(ABC):
    name: str
    level: int

    def __init__(self):
        pass
        # self.module = Module.objects.get_or_create(name=self.name, level=self.level)[0]
