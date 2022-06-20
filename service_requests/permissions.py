from rest_framework.permissions import BasePermission
from django.conf import settings

class GiftryPermission(BasePermission):
    def has_permission(self, request, view):
        return request.headers.get('x-giftry')==settings.X_GIFTRY