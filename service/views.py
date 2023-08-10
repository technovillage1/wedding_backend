from rest_framework import viewsets
from .serializers import ServiceTypeSerializer, ServiceSerializer
from .models import ServiceType, Service

# Create your views here.

class ServiceTypeViewSet(viewsets.ModelViewSet):
    queryset = ServiceType.objects.all()    
    serializer_class = ServiceTypeSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer