from django import forms
from .models import Reservation, Guest
from rooms.models import Room

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'id_number']

class ReservationForm(forms.ModelForm):
    check_in_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    check_out_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    room = forms.ModelChoiceField(queryset=Room.objects.all())

    class Meta:
        model = Reservation
        fields = ['check_in_date', 'check_out_date', 'room']  # Included room
