from rest_framework import serializers

from users.models import User
from .models import MyDevice


class DeviceSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        required=False,
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault(),
    )
    class Meta:
        model = MyDevice
        fields = ('dev_id','reg_id','name','is_active','user')
