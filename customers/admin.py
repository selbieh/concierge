from django.contrib import admin

# Register your models here.
from customers.models import Customer, InvitationCode

admin.site.register(Customer)
admin.site.register(InvitationCode)
