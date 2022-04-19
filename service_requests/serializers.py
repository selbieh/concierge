from rest_framework import serializers

from users.models import User
from .models import ServiceRequest


class ServiceRequestSerializer(serializers.ModelSerializer):
    status = serializers.CharField(default=ServiceRequest.CREATED, allow_null=True, allow_blank=True, read_only=True)
    user = serializers.PrimaryKeyRelatedField(
        required=False,
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault(),
    )
    payment_status = serializers.CharField( allow_null=True, allow_blank=True, read_only=True)


    class Meta:
        fields = '__all__'
        model = ServiceRequest
