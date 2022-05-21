# Generated by Django 3.2.9 on 2022-05-20 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enemy', '0001_initial'),
        ('module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enemy',
            name='source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='module.module', verbose_name='Источник'),
        ),
        migrations.AddField(
            model_name='enemy',
            name='tags',
            field=models.ManyToManyField(related_name='resumes', to='enemy.Tag', verbose_name='Навыки'),
        ),
    ]