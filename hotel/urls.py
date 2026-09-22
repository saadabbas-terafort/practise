from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('api/staff', views.StaffView.as_view(), name="staff"),
    path('api/hotel', views.HotelView.as_view(), name="hotel"),
    path('api/department', views.DepartementView.as_view(), name="depart"),
    path('api/rooms', views.RoomView.as_view(), name="rooms"),
    path('api/guests', views.GuestView.as_view(), name="guests"),
    path('api/bookings', views.BookingView.as_view(), name="bookings"),
    path('api/payments', views.PaymentView.as_view(), name="payments"),
]
