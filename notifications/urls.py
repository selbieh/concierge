from django.urls import path,include

from rest_framework import routers
from .views import DeviceViewSet

router = routers.DefaultRouter()
router.register(r'devices', DeviceViewSet)

urlpatterns = [
    path('fcm/', include(router.urls))

]
