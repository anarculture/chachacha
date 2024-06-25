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
