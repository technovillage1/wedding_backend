from secrets import choice

from django.conf import settings

from config.redis_client import redis_client
from sms_service.utils import send_sms


def generate_otp(length=6):
    return "".join([choice("1234567890") for _ in range(length)])


def send_otp(phone_number):
    otp = generate_otp()
    redis_client.setex(phone_number, settings.OTP_LIFETIME, otp)
    message_body = f"{settings.OTP_MESSAGE} {otp}"
    send_sms(phone_number, message_body)
