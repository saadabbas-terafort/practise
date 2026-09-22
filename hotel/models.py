from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField( max_length=255)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    
class Department(models.Model):
    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        related_name="departments"
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Staff(models.Model):
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="staff_members"
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Room(models.Model):
    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        related_name="rooms"
    )
    room_number = models.CharField(max_length=20)
    room_type = models.CharField(max_length=50)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.room_type


class Guest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Booking(models.Model):
    guest = models.ForeignKey(
        Guest,
        on_delete=models.CASCADE,
        related_name="bookings"
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name="bookings"
    )
    check_in = models.DateField()
    check_out = models.DateField()
    status = models.CharField(max_length=30, default="confirmed")

    def __str__(self):
        return f"{self.guest.name} - {self.room.room_number}"


class Payment(models.Model):
    booking = models.ForeignKey(
        Booking,
        on_delete=models.CASCADE,
        related_name="payments"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=30, default="paid")
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.booking} - {self.amount}"
