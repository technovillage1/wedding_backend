from rest_framework.permissions import BasePermission
from service.models import Service
from .models import Booking


class BookingOrServiceOwner(BasePermission):
    def has_permission(self, request, view):
        service_obj = Service.objects.all()
        booking_obj = Booking.objects.all()
        for s_obj in service_obj:
            for b_obj in booking_obj:
                if request.user == s_obj.owner or request.user == b_obj.user:
                    return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return bool(request.user and
                    request.user.is_authenticated and
                    (request.user == obj.user or request.user == obj.service.owner)
                    )


class IsBookingOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and
                    request.user.is_authenticated and
                    request.user == obj.user)

class IsServiseOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and
                    request.user.is_authenticated and
                    request.user == obj.service.owner)