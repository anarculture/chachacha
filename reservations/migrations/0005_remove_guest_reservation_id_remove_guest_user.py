# Generated by Django 5.0.6 on 2024-06-25 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0004_guest_reservation_id_guest_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='reservation_id',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='user',
        ),
    ]