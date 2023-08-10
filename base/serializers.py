from rest_framework import serializers
from .models import Region, District

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"
        
class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"