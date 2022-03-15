import requests
from allauth.account import app_settings
from django.core import signing
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404
from users.models import User


def custom_confirm(request, key):
    response = requests.post(request.build_absolute_uri(reverse('rest_verify_email')), data={"key": key})
    if response.status_code == 200:
        max_age = 60 * 60 * 24 * app_settings.EMAIL_CONFIRMATION_EXPIRE_DAYS
        pk = signing.loads(key, max_age=max_age, salt=app_settings.SALT)
        user = get_object_or_404(id=pk)
        user.is_active = True
        user.save()
        msg = 'mail confirmed'
    else:
        msg = 'link not found'
    return HttpResponse(msg)
