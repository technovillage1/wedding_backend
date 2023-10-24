from django.db import models
from django.db.models import TextChoices
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework.exceptions import ValidationError

from base.models import BaseModel
from service.models import Service


class BookingTimeChoices(TextChoices):
    MORNING = 'morning', 'Morning'
    AFTERNOON = 'afternoon', 'Afternoon'
    EVENING = 'evening', 'Evening'


class BookingStatuses(TextChoices):
    PENDING = 'pending', 'Pending'
    ACCEPTED = 'accepted', 'Accepted'
    REJECTED = 'rejected', 'Rejected'
    CANCELLED = 'cancelled', 'Cancelled'
    EXPIRED = 'expired', 'Expired'


def validate_future_date(value):
    if value < timezone.now().date():
        raise ValidationError('Booking date cannot be in the past.')


class Booking(BaseModel):
    service = models.ForeignKey("service.Service", related_name="bookings", on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey("users.User", related_name="bookings", on_delete=models.SET_NULL, null=True)
    booking_time = models.CharField(max_length=50, choices=BookingTimeChoices.choices)
    booking_date = models.DateField(validators=[validate_future_date])
    comment = models.TextField(blank=True)
    customer_phone_number = PhoneNumberField()
    suggested_price = models.PositiveIntegerField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=BookingStatuses.choices, default=BookingStatuses.PENDING)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"



class Schedule(BaseModel):
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    time = models.CharField(max_length=50, choices=BookingTimeChoices.choices)
    date = models.DateField()
    booking = models.ForeignKey(Booking, on_delete=models.SET_NULL, null=True)
    is_booked = models.BooleanField(default=False, blank=True)
    
    def __str__(self):
        return self.service.title