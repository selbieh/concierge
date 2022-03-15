from django.db import models
from django.utils.translation import gettext_lazy as _


def upload_logo(instance, filename):
    return "customer/{0}/{1}".format(instance.id, filename)

class Customer(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    logo = models.ImageField(_("avatar"), null=True, upload_to=upload_logo)