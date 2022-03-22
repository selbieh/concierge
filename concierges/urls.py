"""concierges URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from concierges.views import custom_confirm, custom_reset_handler, custom_reset_handler_submit
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/reset/confirm/<str:uid>/<str:token>/', custom_reset_handler, name='password_reset_confirm'),
    path('dj-rest-auth/custom_reset_handler_submit/', custom_reset_handler_submit, name='custom_reset_handler_submit'),
    path('dj-rest-auth/registration/account-confirm-email/<str:key>/', custom_confirm),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('user/', include("users.urls")),
    path('customers/', include('customers.urls')),
    path('services/', include('services.urls')),
    path('docs/', schema_view)
    # url(r'^account/', include('allauth.urls')),
    # path('dj-rest-auth/registration/account-confirm-email/<str:key>/', custom_confirm),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)