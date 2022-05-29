from django.db import models


class PayOrderResponseLog(models.Model):
    opay_response = models.JSONField(default=dict, null=False, blank=False)
    order=models.ForeignKey('service_requests.ServiceRequest',on_delete=models.CASCADE,blank=False,null=False,related_name='pay_order_responses')
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.order.id)

