from rest_framework.viewsets import ModelViewSet

from booking.models import Booking
from booking.permissions import BookingOrServiceOwner
from booking.serializers import BookingSerializer


class BookingViewSet(ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = (BookingOrServiceOwner,)
    http_method_names = ('get', 'post', 'patch')
