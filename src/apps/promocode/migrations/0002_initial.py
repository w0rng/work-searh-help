# Generated by Django 3.2.9 on 2021-12-21 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('promocode', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='activation',
            unique_together={('user', 'promocode')},
        ),
    ]
