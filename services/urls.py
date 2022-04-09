from django.urls import path

from services.views import ListServicesAPI, ListHomeBannerAPI, ListHomePromotionsAPI

app_name = "services"

urlpatterns = [
    path("", ListServicesAPI.as_view(), name="list-services"),
    path("banners/", ListHomeBannerAPI.as_view(), name="list-home-banners"),
    path("promotions/", ListHomePromotionsAPI.as_view(), name="list-home-promotions")
]