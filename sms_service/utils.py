import json
from typing import Optional

import requests

from django.conf import settings


def get_token() -> Optional[str]:
    payload = {'email': settings.ESKIZ_EMAIL,
               'password': settings.ESKIZ_PASSWORD}
    response = requests.post(settings.ESKIZ_LOGIN_URL, json=payload)
    return json.loads(response.text).get('data', {}).get('token')


def send_sms(phone_number, message):
    phone_number = phone_number[1:] if phone_number.startswith("+") else phone_number
    token = get_token()
    headers = {
        'Authorization': f"Bearer {token}"
    }
    payload = {'mobile_phone': phone_number,
               'message': message,
               'from': '4546',
               # 'callback_url': 'http://0000.uz/test.php'
               }
    response = requests.post(settings.ESKIZ_SEND_SMS_URL, json=payload, headers=headers)
