from django.db import models
from django.utils.translation import gettext_lazy as _


def upload_service_image(instance, filename):
    return "service/{0}/{1}".format(instance.id, filename)


def upload_banner_image(instance, filename):
    return "home_banner/{0}/{1}".format(instance.id, filename)


def upload_promotion_image(instance, filename):
    return "promotion/{0}/{1}".format(instance.id, filename)


class Service(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image = models.ImageField(_("image"), null=True, upload_to=upload_service_image)
    price = models.FloatField(null=True, blank=True)
    category = models.ForeignKey("customers.Category", on_delete=models.CASCADE, related_name="category_services")
    integration_rout = models.CharField(blank=True, null=True, max_length=255)
    duration = models.PositiveIntegerField(blank=True, null=True, default=0)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ('order',)
    def __str__(self):
        return self.name


class HomeBanner(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=upload_banner_image, null=True)
    route = models.CharField(max_length=200, null=False, blank=False)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ('order',)


class HomePromotion(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=upload_promotion_image, null=True)
    route = models.CharField(max_length=200, null=False, blank=False)

    order = models.IntegerField(default=0)

    class Meta:
        ordering = ('order',)


class Prerequisite(models.Model):
    name = models.CharField(max_length=300, null=False, blank=False)
    service = models.ForeignKey('services.Service', null=False, blank=False, on_delete=models.CASCADE,
                                related_name='prerequisites')
