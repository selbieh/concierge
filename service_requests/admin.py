from django.contrib import admin
from import_export.admin import ExportMixin

from customers.models import Customer, StaffAssignedCustomersRequests
from notifications.models import UserSavedNotifications
from .models import ServiceRequest, GifteryCallback


class CustomerFilter(admin.SimpleListFilter):
    title = 'Customer filter'
    parameter_name = 'customer'

    def lookups(self, request, model_admin):
        return [(c.id,c.name) for c in Customer.objects.all() ]

    def queryset(self, request, queryset):
        if self.value():

            return queryset.filter(user__customer__id=self.value())
        return queryset


class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ['id','service','user','status']
    autocomplete_fields = ['user','service']
    search_fields = ['requester_mobile']
    list_filter = ['status','payment_status','payment_method',CustomerFilter]
    readonly_fields = ['payment_unique_ident_history','payment_unique_ident','payment_status']

    def get_queryset(self, request):
        qs=super(ServiceRequestAdmin, self).get_queryset(request)
        user = request.user
        assigned=StaffAssignedCustomersRequests.objects.filter(user=user).first()
        if assigned :
            return qs.filter(user__customer__in=assigned.customers.all())
        return qs.none()



admin.site.register(ServiceRequest,ServiceRequestAdmin)
admin.site.register(UserSavedNotifications)
admin.site.register(GifteryCallback)
