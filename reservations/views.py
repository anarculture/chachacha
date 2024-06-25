from django.shortcuts import render, get_object_or_404, redirect
from .models import Reservation
from .forms import ReservacionForm
from .models import Guest

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

# from .forms import GuestForm  # Comment out this line if GuestForm doesn't exist

def guest_list(request):
    guests = Guest.objects.all()
    return render(request, 'reservations/guest_list.html', {'guests': guests})

def guest_detail(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    return render(request, 'reservations/guest_detail.html', {'guest': guest})

# Comment out these views if they use GuestForm
# def guest_create(request):
#     if request.method == 'POST':
#         form = GuestForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('guest_list')
#     else:
#         form = GuestForm()
#     return render(request, 'reservations/guest_form.html', {'form': form})

# def guest_update(request, pk):
#     guest = get_object_or_404(Guest, pk=pk)
#     if request.method == 'POST':
#         form = GuestForm(request.POST, instance=guest)
#         if form.is_valid():
#             form.save()
#             return redirect('guest_list')
#     else:
#         form = GuestForm(instance=guest)
#     return render(request, 'reservations/guest_form.html', {'form': form})

# def guest_delete(request, pk):
#     guest = get_object_or_404(Guest, pk=pk)
#     if request.method == 'POST':
#         guest.delete()
#         return redirect('guest_list')
#     return render(request, 'reservations/guest_confirm_delete.html', {'guest': guest})
