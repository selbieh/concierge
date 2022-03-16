from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from services.models import Service
from services.serializers import ListServicesSerializer


class ListServicesAPI(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ListServicesSerializer
    queryset = Service.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category"]
