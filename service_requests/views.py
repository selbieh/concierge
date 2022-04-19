from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin,ListModelMixin,RetrieveModelMixin
from .models import ServiceRequest

# Create your views here.
from .serializers import ServiceRequestSerializer


class ServiceRequestViewSets(GenericViewSet,CreateModelMixin,ListModelMixin,RetrieveModelMixin):
    serializer_class = ServiceRequestSerializer

    def get_queryset(self):
        return ServiceRequest.objects.filter(user=self.request.user)
