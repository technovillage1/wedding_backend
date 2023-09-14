from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import ServiceType, Service, Attachment, Review


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = "__all__"


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ("rating", "comment", "service", 'user')
        extra_kwargs = {
            "user": {"read_only": True}
        }

    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user


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
    attachments = serializers.ListSerializer(child=AttachmentSerializer())
    rating = serializers.FloatField(read_only=True)

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
            'rating',
            'attachments',
        ]
        extra_kwargs = {
            'id': {"read_only": True},
            'is_confirmed': {"read_only": True},
            'attachments': {"read_only": True},
            'owner': {"read_only": True},
        }

    def create(self, validated_data):
        validated_data['owner'] = self.context.get('request').user
