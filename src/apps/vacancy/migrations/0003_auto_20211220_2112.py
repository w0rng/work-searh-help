# Generated by Django 3.2.9 on 2021-12-20 14:12

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import apps.helpers.models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0002_alter_vacancy_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='description',
            field=models.TextField(default='', verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='price',
            field=apps.helpers.models.PriceField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.0')), django.core.validators.MinValueValidator(Decimal('0.0')), django.core.validators.MinValueValidator(Decimal('0.0'))], verbose_name='Зарплата'),
        ),
    ]
