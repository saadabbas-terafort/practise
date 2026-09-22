from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Staff, Department, Hotel, Room, Guest, Booking, Payment
# Register your models here.
admin.site.register(Staff)
admin.site.register(Department)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Guest)
admin.site.register(Booking)
admin.site.register(Payment)
