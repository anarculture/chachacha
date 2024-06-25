from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['guest', 'room', 'check_in_date', 'check_out_date', 'checked_in']
