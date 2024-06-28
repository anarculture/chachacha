from django.shortcuts import render, get_object_or_404, redirect
from .models import Guest, Reservation
from .forms import GuestForm, ReservationForm
from django.forms import modelformset_factory

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations})

def reservation_detail(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    return render(request, 'reservations/reservation_detail.html', {'reservation': reservation})

def reservation_create(request):
    GuestFormSet = modelformset_factory(Guest, form=GuestForm, extra=1)
    if request.method == 'POST':
        reservation_form = ReservationForm(request.POST)
        guest_formset = GuestFormSet(request.POST, queryset=Guest.objects.none())
        if reservation_form.is_valid() and guest_formset.is_valid():
            new_guest = guest_formset.save()
            reservation = reservation_form.save(commit=False)
            reservation.guest = new_guest[0]
            reservation.save()
            return redirect('reservation_list')
    else:
        reservation_form = ReservationForm()
        guest_formset = GuestFormSet(queryset=Guest.objects.none())
    return render(request, 'reservations/reservation_form.html', {
        'reservation_form': reservation_form,
        'guest_formset': guest_formset
    })

def reservation_update(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        reservation_form = ReservationForm(request.POST, instance=reservation)
        if reservation_form.is_valid():
            reservation_form.save()
            return redirect('reservation_list')
    else:
        reservation_form = ReservationForm(instance=reservation)
    return render(request, 'reservations/reservation_form.html', {'reservation_form': reservation_form})

def reservation_delete(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        reservation.delete()
        return redirect('reservation_list')
    return render(request, 'reservations/reservation_confirm_delete.html', {'reservation': reservation})
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
