from rest_framework.permissions import BasePermission
from service.models import Service


class BookingOrServiceOwner(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated
        )

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