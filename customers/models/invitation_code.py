from django.db import models


class InvitationCode(models.Model):
    code = models.CharField(max_length=150, null=False, blank=False)
    used = models.BooleanField(default=False)
    customer = models.ForeignKey("customers.Customer", on_delete=models.CASCADE, related_name="customer_invitation_codes")