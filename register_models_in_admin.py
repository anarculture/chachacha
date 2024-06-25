import os

# Set project directory
project_dir = '/home/anarculture/code/anarculture/chachacha/hotel_pms'
os.chdir(project_dir)

# Define models to be registered in admin for each app
admin_registrations = {
    'users/admin.py': """\
from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_staff', 'is_admin', 'is_guest']
""",
    'rooms/admin.py': """\
from django.contrib import admin
from .models import Room

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['number', 'room_type', 'is_available']
""",
    'reservations/admin.py': """\
from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['guest', 'room', 'check_in_date', 'check_out_date', 'checked_in']
""",
    'billing/admin.py': """\
from django.contrib import admin
from .models import Invoice

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['reservation', 'amount', 'paid']
""",
    'reporting/admin.py': """\
from django.contrib import admin

# Add your model registrations here
"""
}

# Create or update admin.py files
for path, content in admin_registrations.items():
    full_path = os.path.join(project_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w') as f:
        f.write(content)

print("Models have been registered in the admin interface.")
