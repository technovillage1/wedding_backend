from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView

from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from booking.models import Booking, BookingStatuses
from booking.permissions import BookingOrServiceOwner
from booking.serializers import BookingSerializer, BookingCreateUpdateSerializer

from .serializers import ScheduleSerializer
from .models import Schedule

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    permission_classes = (BookingOrServiceOwner,)
    http_method_names = ('get', 'post', 'patch')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('service', 'user', 'status')


    def get_serializer_class(self):
        if self.action == "create" or self.action == "partial_update":
            return BookingCreateUpdateSerializer
        else:
            return BookingSerializer
        

class BookingAcceptedView(GenericAPIView):
    def patch(self, request, pk):
        obj = get_object_or_404(Booking, pk=pk)
        obj.status = BookingStatuses.ACCEPTED
        obj.save()
        
        return Response(BookingSerializer(obj).data)
        
class BookingRejectedView(GenericAPIView):
    def patch(self, request, pk):
        obj = get_object_or_404(Booking, pk=pk)
        obj.status = BookingStatuses.REJECTED
        obj.save()
        
        return Response(BookingSerializer(obj).data)

class BookingCancelledView(GenericAPIView):
    def patch(self, request, pk):
        obj = get_object_or_404(Booking, pk=pk)
        obj.status = BookingStatuses.CANCELLED
        obj.save()

        return Response(BookingSerializer(obj).data)

class ScheduleAPIView(GenericAPIView):
    def get(self, request):
        obj = Schedule.objects.all()
        serializer = ScheduleSerializer(obj, many=True)
        return Response(serializer.data)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_booked', 'service']
    
    
class ScheduleDetailAPIView(GenericAPIView):
    def get(self, request, pk):
        obj = get_object_or_404(Schedule, pk=pk)
        return Response(ScheduleSerializer(obj).data)

