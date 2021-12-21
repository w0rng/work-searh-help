# Generated by Django 3.2.9 on 2021-12-21 14:53

import apps.helpers.models
from decimal import Decimal
import django.core.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_alter_resume_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='price',
            field=apps.helpers.models.PriceField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.0')), django.core.validators.MinValueValidator(Decimal('0.0')), django.core.validators.MinValueValidator(Decimal('0.0'))], verbose_name='Желаемая зарплата'),
        ),
    ]
