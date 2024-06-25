# Generated by Django 5.0.6 on 2024-06-25 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=50, verbose_name='Apellido')),
                ('room_number', models.CharField(max_length=10, verbose_name='Número de Habitación')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Número de Teléfono')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo Electrónico')),
                ('id_number', models.CharField(max_length=20, verbose_name='Número de Identificación')),
            ],
        ),
    ]