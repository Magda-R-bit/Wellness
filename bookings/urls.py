from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.booking_list, name='booking_list'),
    path('create/', views.create_booking, name='create_booking'),
    path('<int:pk>/', views.booking_detail, name='booking_detail'),
   
]