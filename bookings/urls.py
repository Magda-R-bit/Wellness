from django.urls import path
from .views import BookingListView, BookingCreateView, BookingDetailView

urlpatterns = [
    path('', BookingListView.as_view(), name='bookings'),
    path('create/', BookingCreateView.as_view(), name='create_booking'),
    path('<int:pk>/', BookingDetailView.as_view(), name='booking_detail'),
   
]