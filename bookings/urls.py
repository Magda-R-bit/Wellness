from django.urls import path
from .views import Index
from . import views

urlpatterns = [
    path('', Index.as_view(), name='bookings'),
    path('', views.booking_list, name='booking_list'),
    path('create/', views.create_booking, name='create_booking'),
    path('<int:pk>/', views.booking_detail, name='booking_detail'),
   
]