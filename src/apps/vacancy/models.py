from re import L
from django.db import models
from apps.resume.models import Tag
from helpers.models import PriceField


class Vacancy(models.Model):
    name = models.CharField('Название', max_length=255)
    price = PriceField('Зарплата')
    tags = models.ManyToManyField(Tag, related_name='vacancies', verbose_name='Навыки')
