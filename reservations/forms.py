from django import forms
from .models import Reservation

class ReservacionForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['guest', 'room', 'check_in_date', 'check_out_date', 'checked_in']
        labels = {
            'guest': 'Huésped',
            'room': 'Habitación',
            'check_in_date': 'Fecha de entrada',
            'check_out_date': 'Fecha de salida',
            'checked_in': 'Registrado',
        }
