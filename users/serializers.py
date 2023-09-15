from django.contrib.auth.password_validation import validate_password
from django.db.transaction import atomic
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404

from config.redis_client import redis_client
from users.models import User
from users.utils import send_otp


class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'phone_number', 'full_name', 'role', 'password', 'password2']
        extra_kwargs = {
            'id': {"read_only": True}
        }

    def validate(self, attrs):
        if User.objects.filter(email=attrs['phone_number']).exists():
            raise ValidationError({'detail': 'This phone number already in use!'})
        if attrs['password'] != attrs['password2']:
            raise ValidationError({'detail': 'The passwords are not similar'})
        else:
            validate_password(password=attrs['password'], user=User)
        attrs.pop('password2')
        return attrs

    @atomic
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        send_otp(str(user.phone_number))
        return user


class PhoneConfirmationSerializer(serializers.Serializer):
    phone_number = PhoneNumberField(required=True)
    code = serializers.CharField(required=True)

    def validate(self, attrs):
        phone_number = str(attrs['phone_number'])
        user = get_object_or_404(User, phone_number=phone_number)
        if user.is_phone_confirmed:
            raise ValidationError("The phone number is already confirmed.")
        otp = redis_client.get(phone_number)
        if not otp or otp and str(otp.decode('utf-8')) != attrs['code']:
            redis_client.delete(phone_number)
            send_otp(phone_number)
            raise ValidationError("Confirmation code did not match.\nSent again.")
        attrs["user"] = user
        return attrs

    def create(self, validated_data):
        user = validated_data.get("user")
        user.is_phone_confirmed = True
        user.save(update_fields=["is_phone_confirmed"])
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "phone_number", "full_name", "role", "image", "is_phone_confirmed", "email")
        extra_kwargs = {
            'id': {"read_only": True},
            "phone_number": {"read_only": True},
            "role": {"read_only": True},
            "is_phone_confirmed": {"read_only": True},
            "email": {"read_only": True},
        }
