from rest_framework import viewsets
from .models import MyDevice
from .serializers import DeviceSerializer, UserSavedNotificationsReadSerializer, UserSavedNotificationsUpdateSerializer
from .models import UserSavedNotifications
from rest_framework.mixins import ListModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = MyDevice.objects.all()
    serializer_class = DeviceSerializer


class UserSavedNotificationsViewSet(GenericViewSet, ListModelMixin, UpdateModelMixin):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserSavedNotifications.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method.lower() == 'get':
            return UserSavedNotificationsReadSerializer
        else:
            return UserSavedNotificationsUpdateSerializer