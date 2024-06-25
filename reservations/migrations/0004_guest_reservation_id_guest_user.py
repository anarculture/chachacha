# Generated by Django 5.0.6 on 2024-06-25 08:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_guest'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='reservation_id',
            field=models.CharField(max_length=20, null=True, unique=True, verbose_name='ID de Reservación'),
        ),
        migrations.AddField(
            model_name='guest',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]