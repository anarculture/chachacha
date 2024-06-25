from django import forms
from .models import Invoice

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['reservation', 'amount', 'paid']
        labels = {
            'reservation': 'Reservación',
            'amount': 'Monto',
            'paid': 'Pagado',
        }
