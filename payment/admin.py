from django.contrib import admin

from payment.models import PayOrderResponseLog

class PayOrderResponseLogAdmin(admin.ModelAdmin):
    list_display = ['id','order_id']
    readonly_fields = ['order','opay_response','reference','callback']

admin.site.register(PayOrderResponseLog,PayOrderResponseLogAdmin)
# Register your models here.
