from django.contrib import admin

# Register your models here.
from services.models import Service

admin.site.register(Service)