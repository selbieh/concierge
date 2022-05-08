from django.contrib import admin

from notifications.models import UserSavedNotifications
from .models import ServiceRequest

class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ['id','service','user','status']
    autocomplete_fields = ['user','service']
    search_fields = ['mobile']


admin.site.register(ServiceRequest,ServiceRequestAdmin)
admin.site.register(UserSavedNotifications)
