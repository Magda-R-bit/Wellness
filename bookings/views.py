from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorations import login_required
from .models import Bookings
from .forms import BookingsForm


# Create your views here.

class Index(TemplateView):
    template_name = 'bookings/index.html'


@login_required
def booking_list(request):
    bookings = Bookings.objects.filter(user=request.user)
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})


@login_required
def create_booking(request):
    if request.methode == 'POST':
        form = BookingsForm(request.POST)
        if form.is_valid():
            bookings = form.save(commit=False)
            bookings.user = request.user
            bookings.save()
            return redirect('booking_list')
    else:
        form = BookingsForm()
    return render(reuest, 'bookings/create_booking.html', {'form': form})


@login_required
def booking_detail(request, pk):
    bookings = get_object_or_404(Bookings, pk=pk, user=request.user)
    return render(request, 'bookings/booking_detail.html', {'bookings': bookings})

