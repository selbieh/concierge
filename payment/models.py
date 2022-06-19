from django.db import models


class PayOrderResponseLog(models.Model):
    opay_response = models.JSONField(default=dict, null=False, blank=False)
    order=models.ForeignKey('service_requests.ServiceRequest',on_delete=models.CASCADE,blank=False,null=False,related_name='pay_order_responses')
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    reference=models.CharField(blank=True,null=True,max_length=125)
    callback=models.JSONField(default=dict,blank=True,null=True)
    false_ip_callback=models.BooleanField(default=False)

    def __str__(self):
        return str(self.order.id)



