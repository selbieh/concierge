from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from .filters import ServiceRequestFilter
from .models import ServiceRequest
# Create your views here.
from .serializers import ServiceRequestSerializer, ServiceRequestReadSerializer


class ServiceRequestViewSets(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    serializer_class = ServiceRequestSerializer
    filterset_class = ServiceRequestFilter
    filter_backends = [DjangoFilterBackend]
    permission_classes = []

    def get_queryset(self):
        return ServiceRequest.objects.all()#.filter(user=self.request.user)


    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ServiceRequestReadSerializer
        else:
            return ServiceRequestSerializer
