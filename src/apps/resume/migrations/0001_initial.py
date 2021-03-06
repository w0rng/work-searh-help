# Generated by Django 3.2.9 on 2022-01-23 09:04

import django.core.validators
from django.db import migrations, models
import django_lifecycle.mixins
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=32, primary_key=True, serialize=False, unique=True, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('name', models.CharField(max_length=512, verbose_name='Должность')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цена')),
                ('remote', models.BooleanField(default=False, verbose_name='Удаленная работа')),
                ('city', models.CharField(max_length=50, null=True, verbose_name='Город')),
                ('tags', models.ManyToManyField(related_name='resumes', to='resume.Tag', verbose_name='Навыки')),
            ],
            options={
                'abstract': False,
            },
            bases=(django_lifecycle.mixins.LifecycleModelMixin, models.Model),
        ),
    ]
