from django.db import models
from users.models import User
from rooms.models import Room
from django.conf import settings

class Reservation(models.Model):
    guest = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_guest': True})
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    checked_in = models.BooleanField(default=False)

from django.db import models

class Guest(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Nombre')
    last_name = models.CharField(max_length=50, verbose_name='Apellido')
    room_number = models.CharField(max_length=10, verbose_name='Número de Habitación')
    phone_number = models.CharField(max_length=15, verbose_name='Número de Teléfono')
    email = models.EmailField(verbose_name='Correo Electrónico')
    id_number = models.CharField(max_length=20, verbose_name='Número de Identificación')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
