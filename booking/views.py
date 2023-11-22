from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from booking.models import Booking, BookingStatuses
from booking.permissions import BookingOrServiceOwner
from booking.serializers import BookingSerializer, BookingCreateUpdateSerializer
from .models import Schedule
from .serializers import ScheduleSerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    permission_classes = (BookingOrServiceOwner,)
    http_method_names = ('get', 'post', 'patch')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('service', 'user', 'status')

    def get_serializer_class(self):
        if self.action == "create" or "partial_update":
            return BookingCreateUpdateSerializer
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


class ScheduleAPIView(APIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_booked', 'service']

    def get(self, request):
        obj = Schedule.objects.all()
        serializer = ScheduleSerializer(obj, many=True)
        return Response(serializer.data)


class ScheduleDetailAPIView(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(Schedule, pk=pk)
        return Response(ScheduleSerializer(obj).data)
