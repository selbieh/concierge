from rest_framework import serializers

from services.models import Service


class ListServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"
