from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from booking.models import Booking
from booking.permissions import BookingOrServiceOwner
from booking.serializers import BookingSerializer

from .serializers import ScheduleSerializer
from .models import Schedule

class BookingViewSet(ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = (BookingOrServiceOwner,)
    http_method_names = ('get', 'post', 'patch')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('service', 'user', 'status')

class ScheduleAPIView(APIView):
    def get(self, request):
        obj = Schedule.objects.all()
        serializer = ScheduleSerializer(obj, many=True)
        return Response(serializer.data)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_booked', 'service']
    
    
class ScheduleDetailAPIView(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(Schedule, id=pk)
        return Response(ScheduleSerializer(obj).data)