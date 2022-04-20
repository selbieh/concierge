from rest_framework import viewsets
from .models import MyDevice
from .serializers import DeviceSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = MyDevice.objects.all()
    serializer_class = DeviceSerializer


from django.shortcuts import render

# Create your views here.
