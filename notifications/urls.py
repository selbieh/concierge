from django.urls import path,include

from rest_framework import routers
from .views import DeviceViewSet, UserSavedNotificationsViewSet

router = routers.DefaultRouter()
router.register(r'devices', DeviceViewSet)
router.register(r'user-saved-notifications', UserSavedNotificationsViewSet,basename='UserSavedNotifications')

urlpatterns = [
    path('', include(router.urls)),

]
