from django.contrib import admin
from .models import BulkPushNotifications ,RequestNotificationSettings


class BulkPushNotificationsAdmin(admin.ModelAdmin):
    list_display = ['id','message','added_at']
    autocomplete_fields = ['customer']

admin.site.register(BulkPushNotifications,BulkPushNotificationsAdmin)
admin.site.register(RequestNotificationSettings)
