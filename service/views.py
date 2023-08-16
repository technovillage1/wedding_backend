from rest_framework import viewsets
from .serializers import ServiceTypeSerializer, ServiceSerializer, AttachmentSerializer
from .models import ServiceType, Service, Attachment

# Create your views here.

class ServiceTypeViewSet(viewsets.ModelViewSet):
    queryset = ServiceType.objects.all()    
    serializer_class = ServiceTypeSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer