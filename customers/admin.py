from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from customers.models import Customer, InvitationCode, Category

class InvitationCodeAdmin(ImportExportModelAdmin):
    list_display = ['id','code','used','customer']
    search_fields = ['code']
    list_filter = ['used','customer__name']


admin.site.register(Customer)
admin.site.register(InvitationCode,InvitationCodeAdmin)
admin.site.register(Category)

