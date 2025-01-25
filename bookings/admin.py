from django.contrib import admin
from .models import Bookings

# Register your models here.

@admin.register(Bookings)
class BookingsAdmin(admin.ModelAdmin):
    list_display = ('user', 'item_name', 'check_in', 'check_out', 'total_price', 'created_at')
    list_filter = ('check_in', 'check_out', 'created_at')
    search_fields = ('user_username', 'item_name')