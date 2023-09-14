from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .permissions import ServiceAdminOrReadOnly, AttachmentOwnerOrReadOnly
from .serializers import ServiceTypeSerializer, ServiceSerializer, AttachmentSerializer
from .models import ServiceType, Service, Attachment


class ServiceTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [ServiceAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['region', 'district', 'price', 'people_count']
    search_fields = ['title']
    http_method_names = ('get', 'post', 'patch', 'delete')


class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [AttachmentOwnerOrReadOnly]
