from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .serializers import ServiceTypeSerializer, ServiceSerializer, ReviewSerializator
from .models import ServiceType, Service, Review

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
    
class ReviewAPILict(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializator
    
class ReviewAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializator