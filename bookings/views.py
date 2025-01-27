from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm


# Create your views here.



@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})


@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(reqest, 'bookings/create_booking.html', {'form': form})


@login_required
def booking_detail(request, pk):
    booking = get_object_or_404(Bookings, pk=pk, user=request.user)
    return render(request, 'bookings/booking_detail.html', {'booking': booking})

