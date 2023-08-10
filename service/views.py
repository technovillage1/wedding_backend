from rest_framework import viewsets
from .serializers import ServiceTypeSerializer
from .models import ServiceType

# Create your views here.

class ServiceTypeList(viewsets.ModelViewSet):
    queryset = ServiceType.objects.all()    
    serializer_class = ServiceTypeSerializer