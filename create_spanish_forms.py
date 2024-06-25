import os

# Set project directory
project_dir = '/home/anarculture/code/anarculture/chachacha/hotel_pms'
os.chdir(project_dir)

# Define forms with Spanish field labels
forms_content = {
    'users/forms.py': """\
from django import forms
from .models import User

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff', 'is_admin', 'is_guest']
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
            'is_staff': 'Es empleado',
            'is_admin': 'Es administrador',
            'is_guest': 'Es huésped',
        }
""",
    'rooms/forms.py': """\
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
""",
    'reservations/forms.py': """\
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
""",
    'billing/forms.py': """\
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
"""
}

# Create or update forms.py files
for path, content in forms_content.items():
    full_path = os.path.join(project_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w') as f:
        f.write(content)

print("Forms with Spanish field labels have been created.")
