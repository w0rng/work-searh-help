# Generated by Django 3.2.9 on 2022-05-17 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0004_rename_for_all_users_module_public'),
        ('vacancy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='module.module', verbose_name='Источник'),
        ),
    ]
