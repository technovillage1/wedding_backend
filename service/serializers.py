from rest_framework import serializers
from .models import ServiceType, Service, Review

class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = "__all__"

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"
        
class ReviewSerializator(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"