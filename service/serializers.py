from rest_framework import serializers
from .models import ServiceType, Service, Attachment


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = "__all__"


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = "__all__"
        extra_kwargs = {
            'id': {"read_only": True}
        }

    def update(self, instance, validated_data):
        validated_data.pop('service_id', None)
        return super().update(instance, validated_data)


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            'id',
            'owner',
            'title',
            'description',
            'price',
            'people_count',
            'region',
            'district',
            'address',
            'phone_number',
            'additional_phone_number',
            'telegram',
            'instagram',
            'youtube',
            'is_confirmed',
            'lat',
            'long',
            'attachments',
        ]
        extra_kwargs = {
            'id': {"read_only": True},
            'is_confirmed': {"read_only": True},
            'attachments': {"read_only": True},

        }

    def update(self, instance, validated_data):
        validated_data.pop('owner', None)
        return super().update(instance, validated_data)
