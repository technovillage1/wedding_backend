from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from .models import Booking, BookingStatuses, Schedule


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            'id', 'service', 'booking_time', 'booking_date', 'comment', 'customer_phone_number', 'suggested_price',
            'status'
        )

    def validate(self, attrs):
        if attrs.get("status") and attrs["status"] == BookingStatuses.EXPIRED:
            raise ValidationError({"detail": "Booking status cannot be \"Expired\""})

    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user
        if validated_data["service"].owner == self.context.get('request').user:
            pass  # todo add background task for update schedule instance if status is "Accepted"
        else:
            validated_data['status'] = BookingStatuses.PENDING
        return super().create(validated_data)


class BookingCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'service', 'booking_time', 'booking_date', 'comment', 'customer_phone_number', 'suggested_price')


class ScheduleSerializer(ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"

