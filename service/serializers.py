from rest_framework import serializers
from .models import ServiceType, Service, Attachment

class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = "__all__"

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'attachment', 'attachment_type']
        # read_only_fields = ('service',)

class ServiceSerializer(serializers.ModelSerializer):
    attachments = AttachmentSerializer(many=True, required=False)
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
        read_only_fields=('is_confirmed',)
        
    def create(self, validated_data):
        attachments = validated_data.pop('attachments')
        service = Service.objects.create(**validated_data)
        attachments_to_create = [Attachment(service=service, **data) for data in attachments]
        Attachment.objects.bulk_create(attachments_to_create)
        return service