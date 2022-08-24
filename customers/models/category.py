from django.db import models
from django.utils.translation import gettext_lazy as _


def upload_image(instance, filename):
    return "category/{0}/{1}".format(instance.id, filename)


class Category(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image = models.ImageField(_("image"), null=True, upload_to=upload_image)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ('order',)
    def __str__(self):
        return self.title
