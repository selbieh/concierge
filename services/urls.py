from django.urls import path

from customers.views import ListCategoryAPI
from services.views import ListServicesAPI

app_name = "services"

urlpatterns = [
    path("", ListServicesAPI.as_view(), name="list-services")
]