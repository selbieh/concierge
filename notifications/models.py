from django.db import models
from service_requests.models import ServiceRequest

from django.conf import settings
from django.db import models
from fcm.models import AbstractDevice

class MyDevice(AbstractDevice):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

class BulkPushNotifications(models.Model):
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    message = models.CharField(max_length=125, blank=False, null=False)

    def __str__(self):
        return self.message

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(BulkPushNotifications, self).save(force_insert=False, force_update=False, using=None,
                                                update_fields=None)
        from fcm.utils import get_device_model
        Device = get_device_model()
        Device.objects.all().send_message({'message': self.message})



class RequestNotificationSettings(models.Model):
    previous_status=models.CharField(max_length=25,choices=ServiceRequest.status_choices)
    new_status=models.CharField(max_length=25,choices=ServiceRequest.status_choices)
    message=models.CharField(max_length=125,help_text="تم توصيل طلب رقم {{order_id}}")

    def __str__(self):
        return f'from {self.previous_status} to {self.new_status}'


