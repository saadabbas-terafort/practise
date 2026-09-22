from rest_framework import serializers
from .models import Hotel, Department, Staff, Room, Guest, Booking, Payment
from rest_framework import serializers
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ["id", "name", "email", "phone", "salary"]


class DepartmentSerializer(serializers.ModelSerializer):
    staff_members = StaffSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ["id", "name", "hotel", "staff_members"]


class HotelSerializer(serializers.ModelSerializer):
    departments = DepartmentSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ["id", "name", "address", "phone" , "departments"]


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["id", "hotel", "room_number", "room_type", "price_per_night", "is_available"]


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ["id", "name", "email", "phone", "address"]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "guest", "room", "check_in", "check_out", "status"]


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ["id", "booking", "amount", "payment_method", "payment_status", "paid_at"]
