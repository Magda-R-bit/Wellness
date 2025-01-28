from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DetailView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Booking
from django.shortcuts import redirect
from .forms import BookingForm


# Create your views here.

class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'bookings/bookings.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/create_booking.html'
    
    def form_valid(self, form):
        booking = form.save(commit=False)
        booking.user = self.request.user
        booking.save()
        return redirect('bookings')
    


class BookingDetailView(LoginRequiredMixin, DetailView):
    model = Booking
    template_name = 'bookings/booking_detail.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
