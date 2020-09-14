from django.urls import path

from achiever_auth.authorization.views import (
    registration,
    authorization,
)

urlpatterns = [
    path('/register/', register),
    path('/authorize/', authorize),
]