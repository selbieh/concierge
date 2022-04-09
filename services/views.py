from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from services.models import Service, HomeBanner, HomePromotion
from services.serializers import ListServicesSerializer, ListHomeBannerSerializer


class ListServicesAPI(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ListServicesSerializer
    queryset = Service.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category"]


class ListHomeBannerAPI(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ListHomeBannerSerializer
    queryset = HomeBanner.objects.all()


class ListHomePromotionsAPI(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ListHomeBannerSerializer
    queryset = HomePromotion.objects.all()