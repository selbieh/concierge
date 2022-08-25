from rest_framework import serializers

from notifications.models import UserSavedNotifications
from users.models import User





class UserSavedNotificationsReadSerializer(serializers.ModelSerializer):

    icon=serializers.ImageField(source='setting.icon')

    class Meta:
        model=UserSavedNotifications
        fields='__all__'



class UserSavedNotificationsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSavedNotifications
        fields=('seen',)
