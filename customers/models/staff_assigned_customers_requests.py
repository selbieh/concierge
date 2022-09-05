from django.db import models


class StaffAssignedCustomersRequests(models.Model):
    user=models.OneToOneField('users.User',on_delete=models.CASCADE,blank=False,null=False,unique=True)
    customers=models.ManyToManyField('customers.Customer')


