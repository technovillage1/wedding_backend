from rest_framework import viewsets
from .serializers import ServiceTypeSerializer, ServiceSerializer, AttachmentSerializer
from .models import ServiceType, Service, Attachment
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .serializers import ServiceTypeSerializer, ServiceSerializer
from .models import ServiceType, Service

# Create your views here.

class ServiceTypeViewSet(viewsets.ModelViewSet):
    queryset = ServiceType.objects.all()    
    serializer_class = ServiceTypeSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['region', 'district', 'price', 'people_count']
    search_fields = ['title']

class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer

