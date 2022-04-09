from django.contrib import admin

# Register your models here.
from services.models import Service, HomeBanner, HomePromotion

admin.site.register(Service)
admin.site.register(HomeBanner)
admin.site.register(HomePromotion)