import os

# Set project directory
project_dir = '/home/anarculture/code/anarculture/chachacha/hotel_pms'
os.chdir(project_dir)

# Step 1: Create the Guest model in reservations/models.py
guest_model_content = """\
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
"""

models_path = os.path.join(project_dir, 'reservations/models.py')
with open(models_path, 'a') as f:
    f.write("\n\n" + guest_model_content)

# Step 2: Create the Guest form in reservations/forms.py
guest_form_content = """\
from django import forms
from .models import Guest

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['first_name', 'last_name', 'room_number', 'phone_number', 'email', 'id_number']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'room_number': 'Número de Habitación',
            'phone_number': 'Número de Teléfono',
            'email': 'Correo Electrónico',
            'id_number': 'Número de Identificación',
        }
"""

forms_path = os.path.join(project_dir, 'reservations/forms.py')
with open(forms_path, 'a') as f:
    f.write("\n\n" + guest_form_content)

# Step 3: Create CRUD views for Guest in reservations/views.py
guest_views_content = """\
from django.shortcuts import render, get_object_or_404, redirect
from .models import Guest
from .forms import GuestForm

def guest_list(request):
    guests = Guest.objects.all()
    return render(request, 'reservations/guest_list.html', {'guests': guests})

def guest_detail(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    return render(request, 'reservations/guest_detail.html', {'guest': guest})

def guest_create(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guest_list')
    else:
        form = GuestForm()
    return render(request, 'reservations/guest_form.html', {'form': form})

def guest_update(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == 'POST':
        form = GuestForm(request.POST, instance=guest)
        if form.is_valid():
            form.save()
            return redirect('guest_list')
    else:
        form = GuestForm(instance=guest)
    return render(request, 'reservations/guest_form.html', {'form': form})

def guest_delete(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == 'POST':
        guest.delete()
        return redirect('guest_list')
    return render(request, 'reservations/guest_confirm_delete.html', {'guest': guest})
"""

views_path = os.path.join(project_dir, 'reservations/views.py')
with open(views_path, 'a') as f:
    f.write("\n\n" + guest_views_content)

# Step 4: Set up URL patterns for Guest in reservations/urls.py
guest_urls_content = """\
from django.urls import path
from . import views

urlpatterns = [
    path('guests/', views.guest_list, name='guest_list'),
    path('guests/<int:pk>/', views.guest_detail, name='guest_detail'),
    path('guests/new/', views.guest_create, name='guest_create'),
    path('guests/<int:pk>/edit/', views.guest_update, name='guest_update'),
    path('guests/<int:pk>/delete/', views.guest_delete, name='guest_delete'),
    # Add existing reservations URLs here
]
"""

urls_path = os.path.join(project_dir, 'reservations/urls.py')
with open(urls_path, 'a') as f:
    f.write("\n\n" + guest_urls_content)

# Step 5: Create templates for Guest in reservations/templates/reservations/
templates_content = {
    'guest_list.html': """\
<!DOCTYPE html>
<html>
<head>
    <title>Huéspedes</title>
</head>
<body>
    <h1>Huéspedes</h1>
    <a href="{% url 'guest_create' %}">Crear nuevo huésped</a>
    <ul>
        {% for guest in guests %}
            <li>
                <a href="{% url 'guest_detail' guest.pk %}">{{ guest.first_name }} {{ guest.last_name }}</a>
                <a href="{% url 'guest_update' guest.pk %}">Editar</a>
                <a href="{% url 'guest_delete' guest.pk %}">Eliminar</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
""",
    'guest_detail.html': """\
<!DOCTYPE html>
<html>
<head>
    <title>Detalle del Huésped</title>
</head>
<body>
    <h1>Detalle del Huésped</h1>
    <p>Nombre: {{ guest.first_name }}</p>
    <p>Apellido: {{ guest.last_name }}</p>
    <p>Número de Habitación: {{ guest.room_number }}</p>
    <p>Número de Teléfono: {{ guest.phone_number }}</p>
    <p>Correo Electrónico: {{ guest.email }}</p>
    <p>Número de Identificación: {{ guest.id_number }}</p>
    <a href="{% url 'guest_update' guest.pk %}">Editar</a>
    <a href="{% url 'guest_delete' guest.pk %}">Eliminar</a>
</body>
</html>
""",
    'guest_form.html': """\
<!DOCTYPE html>
<html>
head>
    <title>Formulario de Huésped</title>
</head>
<body>
    <h1>Formulario de Huésped</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Guardar</button>
    </form>
</body>
</html>
""",
    'guest_confirm_delete.html': """\
<!DOCTYPE html>
<html>
<head>
    <title>Confirmar Eliminación</title>
</head>
<body>
    <h1>Confirmar Eliminación</h1>
    <p>¿Estás seguro de que quieres eliminar el huésped "{{ guest.first_name }} {{ guest.last_name }}"?</p>
    <form method="post">
        {% csrf_token %}
        <button type="submit">Confirmar</button>
    </form>
</body>
</html>
"""
}

templates_dir = os.path.join(project_dir, 'reservations/templates/reservations')
os.makedirs(templates_dir, exist_ok=True)

for filename, content in templates_content.items():
    template_path = os.path.join(templates_dir, filename)
    with open(template_path, 'w') as f:
        f.write(content)

print("Guest functionality has been set up.")
