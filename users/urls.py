from django.urls import path

from users.views import GetOrUpdateUserAPI

app_name = "users"

urlpatterns = [
    path("profile/", GetOrUpdateUserAPI.as_view(), name="user-profile"),
]