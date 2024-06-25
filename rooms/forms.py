from django import forms
from .models import Room

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['number', 'room_type', 'is_available']
        labels = {
            'number': 'Número',
            'room_type': 'Tipo de habitación',
            'is_available': 'Está disponible',
        }
