from django.db import models
from apps.helpers.models import CreatedModel, UUIDModel
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator


User = get_user_model()


class Tag(models.Model):
    name = models.CharField('Название', unique=True, primary_key=True, max_length=32)

    def __str__(self):
        return self.name


class Resume(UUIDModel, CreatedModel):
    user = models.OneToOneField(User, models.CASCADE, verbose_name='Пользователь', related_name='resume')
    name = models.CharField('Должность', max_length=512)
    tags = models.ManyToManyField(Tag, related_name='resumes', verbose_name='Навыки')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return f'{self.user} {self.name}'
