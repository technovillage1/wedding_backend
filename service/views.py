from django.db.models import Avg
from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .filters import ServiceFilter
from .permissions import ServiceAdminOrReadOnly, AttachmentOwnerOrReadOnly
from .serializers import ServiceTypeSerializer, ServiceSerializer, AttachmentSerializer, ReviewSerializer
from .models import ServiceType, Service, Attachment, Review


class ServiceTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.annotate(rating=Avg('reviews__rating'))
    serializer_class = ServiceSerializer
    permission_classes = [ServiceAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ServiceFilter
    # filterset_fields = ['region', 'district', 'price', 'people_count']
    search_fields = ['title']
    ordering_fields = ['title', 'price', 'people_count']
    http_method_names = ('get', 'post', 'patch', 'delete')

    # def list(self, request, *args, **kwargs):



class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [AttachmentOwnerOrReadOnly]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'post')
