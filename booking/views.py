from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from booking.models import Booking, BookingStatuses
from booking.permissions import BookingOrServiceOwner
from booking.serializers import BookingSerializer, BookingStatusSerializer


class BookingViewSet(ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = (BookingOrServiceOwner,)
    http_method_names = ('get', 'post', 'patch')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('service', 'user', 'status')

    def get_serializer_class(self):
        if self.action == "create" or "partial_update":
            return BookingStatusSerializer
        else:
            return BookingSerializer
        

class BookingAcceptedView(APIView):
    def patch(self, request, pk):
        obj = get_object_or_404(Booking, pk=pk)
        obj.status = BookingStatuses.ACCEPTED
        obj.save()
        
        return Response(BookingSerializer(obj).data)
        
class BookingRejectedView(APIView):
    def patch(self, request, pk):
        obj = get_object_or_404(Booking, pk=pk)
        obj.status = BookingStatuses.REJECTED
        obj.save()
        
        return Response(BookingSerializer(obj).data)

class BookingCancelledView(APIView):
    def patch(self, request, pk):
        obj = get_object_or_404(Booking, pk=pk)
        obj.status = BookingStatuses.CANCELLED
        obj.save()

        return Response(BookingSerializer(obj).data)
