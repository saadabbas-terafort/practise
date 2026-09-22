from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Hotel, Staff, Department, Room, Guest, Booking, Payment
from rest_framework.views import APIView
from .serializers import (
    StaffSerializer,
    DepartmentSerializer,
    HotelSerializer,
    RoomSerializer,
    GuestSerializer,
    BookingSerializer,
    PaymentSerializer,
)
from rest_framework.response import Response
from datetime import date
# Create your views here.

class HotelView(APIView):
    def get(self, request):
        hotels = Hotel.objects.all()
        hotel = HotelSerializer(hotels, many=True)
        return Response(hotel.data)

    def post(self, request):
        hotels = Hotel.objects.bulk_create([
            Hotel(name="Pearl Continental", address="Mall Road, Lahore", phone="042111505505"),
            Hotel(name="Serena Hotel", address="Khayaban-e-Suhrwardy, Islamabad", phone="051111133133"),
            Hotel(name="Avari Towers", address="Fatima Jinnah Road, Karachi", phone="021111282747"),
            Hotel(name="Ramada Multan", address="Abdali Road, Multan", phone="061111726232"),
            Hotel(name="Nishat Hotel", address="Gulberg III, Lahore", phone="042111646835"),
        ])
        hotel = HotelSerializer(hotels, many=True)
        return Response(hotel.data)
    
    
class StaffView(APIView):
    def get(self , request):
        Stafff = Staff.objects.all()
        staff = StaffSerializer(Stafff , many = True)
        return Response(staff.data)
    
class DepartementView(APIView):
    def get(self , request):
        depart = Department.objects.all()
        D_ment = DepartmentSerializer(depart , many= True)
        return Response(D_ment.data)


class RoomView(APIView):
    def get(self, request):
        rooms = Room.objects.all()
        room = RoomSerializer(rooms, many=True)
        return Response(room.data)

    def post(self, request):
        hotel , created = Hotel.objects.get_or_create(
            name="Pearl Continental",
            defaults={"address": "Mall Road, Lahore", "phone": "042111505505"}
        )
        rooms = Room.objects.bulk_create([
            Room(hotel=hotel, room_number="101", room_type="Single", price_per_night=8500),
            Room(hotel=hotel, room_number="102", room_type="Double", price_per_night=12000),
            Room(hotel=hotel, room_number="201", room_type="Deluxe", price_per_night=18000),
            Room(hotel=hotel, room_number="202", room_type="Suite", price_per_night=25000),
            Room(hotel=hotel, room_number="301", room_type="Family", price_per_night=22000),
        ])
        room = RoomSerializer(rooms, many=True)
        return Response(room.data)


class GuestView(APIView):
    def get(self, request):
        guests = Guest.objects.all()
        guest = GuestSerializer(guests, many=True)
        return Response(guest.data)

    def post(self, request):
        guests = Guest.objects.bulk_create([
            Guest(name="Ali Khan", email="ali@example.com", phone="03001234567", address="Lahore"),
            Guest(name="Sara Ahmed", email="sara@example.com", phone="03011234567", address="Islamabad"),
            Guest(name="Usman Raza", email="usman@example.com", phone="03021234567", address="Karachi"),
            Guest(name="Ayesha Noor", email="ayesha@example.com", phone="03031234567", address="Multan"),
            Guest(name="Bilal Shah", email="bilal@example.com", phone="03041234567", address="Faisalabad"),
        ])
        guest = GuestSerializer(guests, many=True)
        return Response(guest.data)


class BookingView(APIView):
    def get(self, request):
        bookings = Booking.objects.all()
        booking = BookingSerializer(bookings, many=True)
        return Response(booking.data)

    def post(self, request):
        hotel, _ = Hotel.objects.get_or_create(
            name="Pearl Continental",
            defaults={"address": "Mall Road, Lahore", "phone": "042111505505"}
        )
        room_defaults = [
            ("101", "Single", 8500),
            ("102", "Double", 12000),
            ("201", "Deluxe", 18000),
            ("202", "Suite", 25000),
            ("301", "Family", 22000),
        ]
        rooms = [
            Room.objects.get_or_create(
                hotel=hotel,
                room_number=room_number,
                defaults={"room_type": room_type, "price_per_night": price}
            )[0]
            for room_number, room_type, price in room_defaults
        ]
        guest_defaults = [
            ("Ali Khan", "ali@example.com", "03001234567", "Lahore"),
            ("Sara Ahmed", "sara@example.com", "03011234567", "Islamabad"),
            ("Usman Raza", "usman@example.com", "03021234567", "Karachi"),
            ("Ayesha Noor", "ayesha@example.com", "03031234567", "Multan"),
            ("Bilal Shah", "bilal@example.com", "03041234567", "Faisalabad"),
        ]
        guests = [
            Guest.objects.get_or_create(
                email=email,
                defaults={"name": name, "phone": phone, "address": address}
            )[0]
            for name, email, phone, address in guest_defaults
        ]
        bookings = Booking.objects.bulk_create([
            Booking(guest=guests[0], room=rooms[0], check_in=date(2026, 10, 1), check_out=date(2026, 10, 3)),
            Booking(guest=guests[1], room=rooms[1], check_in=date(2026, 10, 4), check_out=date(2026, 10, 6)),
            Booking(guest=guests[2], room=rooms[2], check_in=date(2026, 10, 7), check_out=date(2026, 10, 10)),
            Booking(guest=guests[3], room=rooms[3], check_in=date(2026, 10, 11), check_out=date(2026, 10, 14)),
            Booking(guest=guests[4], room=rooms[4], check_in=date(2026, 10, 15), check_out=date(2026, 10, 18)),
        ])
        booking = BookingSerializer(bookings, many=True)
        return Response(booking.data)


class PaymentView(APIView):
    def get(self, request):
        payments = Payment.objects.all()
        payment = PaymentSerializer(payments, many=True)
        return Response(payment.data)

    def post(self, request):
        if Booking.objects.count() < 5:
            BookingView().post(request)
        bookings = Booking.objects.all()[:5]
        payments = Payment.objects.bulk_create([
            Payment(booking=bookings[0], amount=17000, payment_method="Cash"),
            Payment(booking=bookings[1], amount=24000, payment_method="Card"),
            Payment(booking=bookings[2], amount=54000, payment_method="Bank Transfer"),
            Payment(booking=bookings[3], amount=75000, payment_method="Card"),
            Payment(booking=bookings[4], amount=66000, payment_method="Cash"),
        ])
        payment = PaymentSerializer(payments, many=True)
        return Response(payment.data)
