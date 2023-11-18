from rest_framework.serializers import ModelSerializer

from .models import Booking, BookingStatuses


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            'id', 'service', 'booking_time', 'booking_date', 'comment', 'customer_phone_number', 'suggested_price',
            'status'
        )

    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user
        validated_data['status'] = BookingStatuses.PENDING
        return super().create(validated_data)

class BookingStatusSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'service', 'booking_time', 'booking_date', 'comment', 'customer_phone_number', 'suggested_price')
