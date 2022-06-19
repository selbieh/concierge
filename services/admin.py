from django.contrib import admin

# Register your models here.
from services.models import Service, HomeBanner, HomePromotion,Prerequisite


class ServiceAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id','name']
    list_filter = ['category']


admin.site.register(Service,ServiceAdmin)
admin.site.register(HomeBanner)
admin.site.register(HomePromotion)
admin.site.register(Prerequisite)