# Generated by Django 3.2.9 on 2021-12-19 14:35

from django.db import migrations, models
import django_lifecycle.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Promocode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=32, unique=True, verbose_name='Промокод')),
                ('max_activations', models.PositiveSmallIntegerField(default=1, verbose_name='Максимум активаций')),
                ('count_activations', models.PositiveSmallIntegerField(default=0, verbose_name='Всего активаций')),
            ],
            options={
                'verbose_name': 'Промокод',
                'verbose_name_plural': 'Промокоды',
            },
            bases=(django_lifecycle.mixins.LifecycleModelMixin, models.Model),
        ),
    ]