from django.urls import path,include
from .views import ServiceRequestViewSets ,GifteryCallbackView
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('service-request',ServiceRequestViewSets,basename='service-request')

app_name = "service_requests"

urlpatterns = [
    path('',include(router.urls)),
    path('giftry-call-back/',GifteryCallbackView.as_view())
]