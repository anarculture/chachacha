from django.contrib import admin
from .models import Reservation

class ReservationAdmin(admin.ModelAdmin):
    list_display = ['guest', 'room', 'check_in_date', 'check_out_date', 'checked_in']  # Ensure checked_in is listed

admin.site.register(Reservation, ReservationAdmin)
