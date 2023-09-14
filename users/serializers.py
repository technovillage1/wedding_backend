from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from users.models import User


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
            raise ValidationError({'detail': 'This email already in use!'})
        if attrs['password'] != attrs['password2']:
            raise ValidationError({'detail': 'The passwords are not similar'})
        else:
            validate_password(password=attrs['password'], user=User)
        attrs.pop('password2')
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
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
