from django import forms
from .models import Bookings

class BookingsFrom(forms.ModelForm):
    class Meta:
        model = Bookingsfields = ['item_name', 'check_in', 'check_out']
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
        }