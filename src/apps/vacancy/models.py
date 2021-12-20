from django.db import models
from apps.resume.models import Tag


class Vacancy(models.Model):
    name = models.CharField('Название', max_length=255)
    price = models.DecimalField('Зарплата', max_digits=10, decimal_places=2)
    tags = models.ManyToManyField(Tag, related_name='vacancies', verbose_name='Навыки')
