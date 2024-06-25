import os

# Set project directory
project_dir = '/home/anarculture/code/anarculture/chachacha/hotel_pms'
os.chdir(project_dir)

# Define views content for each app
views_content = {
    'users/views.py': """\
from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from .forms import UsuarioForm

def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'users/user_detail.html', {'user': user})

def user_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UsuarioForm()
    return render(request, 'users/user_form.html', {'form': form})

def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UsuarioForm(instance=user)
    return render(request, 'users/user_form.html', {'form': form})

def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'users/user_confirm_delete.html', {'user': user})
""",
    'reservations/views.py': """\
from django.shortcuts import render, get_object_or_404, redirect
from .models import Reservation
from .forms import ReservacionForm

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations})

def reservation_detail(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    return render(request, 'reservations/reservation_detail.html', {'reservation': reservation})

def reservation_create(request):
    if request.method == 'POST':
        form = ReservacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')
    else:
        form = ReservacionForm()
    return render(request, 'reservations/reservation_form.html', {'form': form})

def reservation_update(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        form = ReservacionForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')
    else:
        form = ReservacionForm(instance=reservation)
    return render(request, 'reservations/reservation_form.html', {'form': form})

def reservation_delete(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        reservation.delete()
        return redirect('reservation_list')
    return render(request, 'reservations/reservation_confirm_delete.html', {'reservation': reservation})
""",
    'billing/views.py': """\
from django.shortcuts import render, get_object_or_404, redirect
from .models import Invoice
from .forms import FacturaForm

def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'billing/invoice_list.html', {'invoices': invoices})

def invoice_detail(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    return render(request, 'billing/invoice_detail.html', {'invoice': invoice})

def invoice_create(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
    else:
        form = FacturaForm()
    return render(request, 'billing/invoice_form.html', {'form': form})

def invoice_update(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == 'POST':
        form = FacturaForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
    else:
        form = FacturaForm(instance=invoice)
    return render(request, 'billing/invoice_form.html', {'form': form})

def invoice_delete(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == 'POST':
        invoice.delete()
        return redirect('invoice_list')
    return render(request, 'billing/invoice_confirm_delete.html', {'invoice': invoice})
""",
    'reporting/views.py': """\
from django.shortcuts import render, get_object_or_404, redirect

def report_list(request):
    # Placeholder for actual report objects
    reports = []
    return render(request, 'reporting/report_list.html', {'reports': reports})

def report_detail(request, pk):
    # Placeholder for actual report object
    report = {}
    return render(request, 'reporting/report_detail.html', {'report': report})

def report_create(request):
    if request.method == 'POST':
        # Placeholder for form processing logic
        return redirect('report_list')
    else:
        # Placeholder for form instantiation
        form = {}
    return render(request, 'reporting/report_form.html', {'form': form})

def report_update(request, pk):
    # Placeholder for actual report object
    report = {}
    if request.method == 'POST':
        # Placeholder for form processing logic
        return redirect('report_list')
    else:
        # Placeholder for form instantiation
        form = {}
    return render(request, 'reporting/report_form.html', {'form': form})

def report_delete(request, pk):
    # Placeholder for actual report object
    report = {}
    if request.method == 'POST':
        # Placeholder for delete logic
        return redirect('report_list')
    return render(request, 'reporting/report_confirm_delete.html', {'report': report})
"""
}

# Create directories and files for views
for path, content in views_content.items():
    full_path = os.path.join(project_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w') as f:
        f.write(content)

print("Views for each app have been created.")
