from django.urls import path,include

from rest_framework import routers
from .views import  UserSavedNotificationsViewSet

router = routers.DefaultRouter()
router.register(r'user-saved-notifications', UserSavedNotificationsViewSet,basename='UserSavedNotifications')

urlpatterns = [
    path('', include(router.urls)),

]
