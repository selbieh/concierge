from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import ServiceRequest
# Create your views here.
from .serializers import ServiceRequestSerializer


class ServiceRequestViewSets(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    filter_backends = [DjangoFilterBackend]
    serializer_class = ServiceRequestSerializer
    filterset_fields = ['status']

    def get_queryset(self):
        return ServiceRequest.objects.filter(user=self.request.user)
