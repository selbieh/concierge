from django.db import models


class InvitationCode(models.Model):
    code = models.CharField(max_length=150, null=False, blank=False,unique=True)
    used = models.BooleanField(default=False)
    customer = models.ForeignKey("customers.Customer", on_delete=models.CASCADE, related_name="customer_invitation_codes")

    def __str__(self):
        return f'{self.code}------>{self.customer.name}'