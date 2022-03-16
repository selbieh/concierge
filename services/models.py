from django.db import models
from django.utils.translation import gettext_lazy as _


def upload_service_image(instance, filename):
    return "service/{0}/{1}".format(instance.id, filename)


class Service(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image = models.ImageField(_("image"), null=True, upload_to=upload_service_image)
    price = models.FloatField()
    category = models.ForeignKey("customers.Category", on_delete=models.CASCADE, related_name="category_services")