# rooms/models.py
from django.db import models

class Room(models.Model):
    number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)
