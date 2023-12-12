from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from booking.models import Booking, BookingStatuses
from booking.permissions import BookingOrServiceOwner, IsServiseOwner, IsBookingOwner
from booking.serializers import BookingSerializer, BookingCreateUpdateSerializer
from .models import Schedule
from .serializers import ScheduleSerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    http_method_names = ('get', 'post', 'patch')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('service', 'user', 'status')

    def get_serializer_class(self):
        if self.action == "create" or self.action == "partial_update":
            return BookingCreateUpdateSerializer
        else:
            return BookingSerializer
    
    def get_permissions(self):
        if self.action == "create":
            permission_classes = [IsAuthenticated]

        elif self.action == "list" or self.action == "retrieve":
            permission_classes = [BookingOrServiceOwner]
        
        elif self.action == "partial_update":
            permission_classes = [IsBookingOwner]
            
        return [permission() for permission in permission_classes]

class BookingAcceptedView(GenericAPIView):
    serializer_class = BookingSerializer
    permission_classes = (IsServiseOwner,)
    def patch(self, request, pk):
        obj = get_object_or_404(Booking, pk=pk)
        self.check_object_permissions(request, obj)
        obj.status = BookingStatuses.ACCEPTED
        obj.save()

        return Response(BookingSerializer(obj).data)


class BookingRejectedView(GenericAPIView):
    serializer_class = BookingSerializer
    permission_classes = (IsBookingOwner,)
    def patch(self, request, pk):
        obj = get_object_or_404(Booking, pk=pk)
        self.check_object_permissions(request, obj)
        obj.status = BookingStatuses.REJECTED
        obj.save()

        return Response(BookingSerializer(obj).data)


class BookingCancelledView(GenericAPIView):
    serializer_class = BookingSerializer
    permission_classes = (IsServiseOwner,)
    def patch(self, request, pk):
        obj = get_object_or_404(Booking, pk=pk)
        self.check_object_permissions(request, obj)
        obj.status = BookingStatuses.CANCELLED
        obj.save()

        return Response(BookingSerializer(obj).data)


class ScheduleAPIView(ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_booked', 'service']


class ScheduleDetailAPIView(GenericAPIView):
    serializer_class = ScheduleSerializer

    def get(self, request, pk):
        obj = get_object_or_404(Schedule, pk=pk)
        return Response(ScheduleSerializer(obj).data)
