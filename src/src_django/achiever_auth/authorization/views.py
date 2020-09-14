from rest_framework.decorators import api_view
from django.http.response import HttpResponse

from achiever_auth.core.models import (
    User
)


def is_user_exists(email: str, phone_number: str):
    if email and phone_number:
        return User.objects \
            .filter(email=email, phone_number=phone_number) \
            .exists()
    elif email:
        return User.objects \
            .filter(email=email) \
            .exists()
    elif phone_number:
        return User.objects \
            .filter(phone_number=phone_number) \
            .exists()
    return False


@api_view(['POST'])
def register(request):
    email = request.data.get('email', None)
    phone_number = request.data.get('phone_number', None)
    password = request.data.get('password', None)

    if is_user_exists(email, phone_number):
        return HttpResponse(description='User with ',status=409)


@api_view(['POST'])
def authorize(request):
    email = request.data.get('email', None)
    phone_number = request.data.get('phone_number', None)
    password = request.data.get('password', None)
