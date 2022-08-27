from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .filters import ServiceRequestFilter
from .models import ServiceRequest, GifteryCallback
# Create your views here.
from .permissions import GiftryPermission
from .serializers import ServiceRequestSerializer, ServiceRequestReadSerializer, GifteryCallbackSerializer


class ServiceRequestViewSets(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    serializer_class = ServiceRequestSerializer
    filterset_class = ServiceRequestFilter
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        return ServiceRequest.objects.filter(user=self.request.user)


    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ServiceRequestReadSerializer
        else:
            return ServiceRequestSerializer




class GifteryCallbackView(CreateAPIView,ListAPIView):
    serializer_class =GifteryCallbackSerializer

    def get_queryset(self):
        return GifteryCallback.objects.filter(user=self.request.user)

    def get_permissions(self):
        if self.request.method.lower() == 'get':
            return [IsAuthenticated()]
        else:
            return [GiftryPermission()]



