import os

# Set project directory
project_dir = '/home/anarculture/code/anarculture/chachacha/hotel_pms'
os.chdir(project_dir)

# Step 5: Update settings.py
settings_path = os.path.join(project_dir, 'hotel_pms', 'settings.py')
installed_apps_line = "\nINSTALLED_APPS += ['users', 'rooms', 'reservations', 'billing', 'reporting']\n"
auth_user_model_line = "AUTH_USER_MODEL = 'users.User'\n"

with open(settings_path, 'a') as f:
    f.write(installed_apps_line)
    f.write(auth_user_model_line)

# Step 6: Create Models
models_content = {
    'users/models.py': """\
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_guest = models.BooleanField(default=False)
""",
    'rooms/models.py': """\
from django.db import models

class Room(models.Model):
    number = models.CharField(max_length=10)
    room_type = models.CharField(maxlength=50)
    is_available = models.BooleanField(default=True)
""",
    'reservations/models.py': """\
from django.db import models
from users.models import User
from rooms.models import Room

class Reservation(models.Model):
    guest = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_guest': True})
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    checked_in = models.BooleanField(default=False)
""",
    'billing/models.py': """\
from django.db import models
from reservations.models import Reservation

class Invoice(models.Model):
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
"""
}

for path, content in models_content.items():
    app_path = os.path.join(project_dir, os.path.dirname(path))
    os.makedirs(app_path, exist_ok=True)
    with open(os.path.join(project_dir, path), 'w') as f:
        f.write(content)

# Step 7: Create Views and URLs for reservations app
views_content = """\
from django.shortcuts import render, get_object_or_404
from .models import Reservation

def check_in(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    reservation.checked_in = True
    reservation.save()
    return render(request, 'reservations/check_in.html', {'reservation': reservation})

def check_out(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    reservation.checked_in = False
    reservation.save()
    return render(request, 'reservations/check_out.html', {'reservation': reservation})
"""

urls_content = """\
from django.urls import path
from . import views

urlpatterns = [
    path('check_in/<int:reservation_id>/', views.check_in, name='check_in'),
    path('check_out/<int:reservation_id>/', views.check_out, name='check_out'),
]
"""

os.makedirs(os.path.join('reservations', 'templates', 'reservations'), exist_ok=True)
with open('reservations/views.py', 'w') as f:
    f.write(views_content)
with open('reservations/urls.py', 'w') as f:
    f.write(urls_content)

# Include reservations URLs in the main urls.py
main_urls_path = os.path.join('hotel_pms', 'urls.py')
with open(main_urls_path, 'a') as f:
    f.write("\nfrom django.urls import include, path\n")
    f.write("urlpatterns += [\n    path('reservations/', include('reservations.urls')),\n]\n")

print("Project setup complete. Don't forget to run migrations and create a superuser.")
