from django.db import models
from apps.resume.models import Tag
from django.core.validators import MinValueValidator


class Vacancy(models.Model):
    name = models.CharField('Название', max_length=255)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0)]
    )
    tags = models.ManyToManyField(Tag, related_name='vacancies', verbose_name='Навыки')
    description = models.TextField('Описание')
    city = models.CharField('Город', max_length=50, null=True)
    remote = models.BooleanField('Удаленная работа', default=False)
