from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from customers.serializers import ListCategorySerializer
from customers.models import Category


class ListCategoryAPI(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ListCategorySerializer
    queryset = Category.objects.all()
