from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from customers.models import Customer, InvitationCode, Category, StaffAssignedCustomersRequests


class InvitationCodeAdmin(ImportExportModelAdmin):
    list_display = ['id','code','used','customer']
    search_fields = ['code']
    list_filter = ['used','customer__name']
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    search_fields = ['name']

class StaffAssignedCustomersRequestsAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customers','user']
    list_display = ['id','user']

admin.site.register(Customer,CustomerAdmin)
admin.site.register(StaffAssignedCustomersRequests,StaffAssignedCustomersRequestsAdmin)
admin.site.register(InvitationCode,InvitationCodeAdmin)
admin.site.register(Category)

