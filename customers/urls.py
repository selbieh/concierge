from django.urls import path

from customers.views import ListCategoryAPI

app_name = "customers"

urlpatterns = [
    path("list_categories/", ListCategoryAPI.as_view(), name="list-categories")
]