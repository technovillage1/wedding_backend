from rest_framework import viewsets
from rest_framework import generics, mixins
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
    
class ReviewListAPIView(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializator

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    
class ReviewDestroyAPIView(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializator

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)