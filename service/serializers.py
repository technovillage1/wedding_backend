from rest_framework import serializers
from .models import ServiceType

class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = ['id', 'name', 'created_at', 'updated_at']