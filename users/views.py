from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.serializers import ReadUserDataSerializer, UpdateUserSerializer


class GetOrUpdateUserAPI(RetrieveAPIView, UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = ReadUserDataSerializer
    pagination_class = None

    def get_object(self):
        obj = self.request.user
        return obj

    def get_serializer_class(self):
        if self.request.method in ["PATCH", "PUT"]:
            return UpdateUserSerializer
        return ReadUserDataSerializer
