from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField



class ServiceRequest(models.Model):
    # payment status
    INITIATED = 'initiated'
    PAID = 'paid'
    NOT_REQUIRED = 'not required'
    # order status
    CREATED = 'created'
    WAITING_PAYMENT = 'waiting payment'
    IN_PROCESS = 'in process'
    CANCELED_BY_USER = 'canceled'
    WAITING_PRICING = 'waiting pricing'
    DONE = 'done'
    # payment methods
    CASH = 'cash'
    CARD = 'card'

    payment_status_choices = [
        (INITIATED, INITIATED),
        (PAID, PAID),
        (NOT_REQUIRED, NOT_REQUIRED),
    ]
    status_choices = [
        (CREATED, CREATED),
        (WAITING_PAYMENT, WAITING_PAYMENT),
        (IN_PROCESS, IN_PROCESS),
        (CANCELED_BY_USER, CANCELED_BY_USER),
        (DONE, DONE),
    ]
    payment_methods_choices = [
        (CASH, CASH),
        (CARD, CARD)
    ]

    status = models.CharField(blank=False, null=False, max_length=25, choices=status_choices)
    payment_status = models.CharField(blank=True, null=True, max_length=25, choices=payment_status_choices)
    payment_method = models.CharField(blank=False, null=False, max_length=25, choices=payment_methods_choices)
    service = models.ForeignKey('services.Service', blank=False, null=False, on_delete=models.CASCADE,
                                related_name='service_requests')
    user = models.ForeignKey('users.User', blank=False, null=False, on_delete=models.CASCADE,
                             related_name='user_service_requests')
    price = models.FloatField(null=True, blank=True, max_length=125)
    user_notes = models.TextField(blank=True, null=True)
    operation_notes = models.TextField(blank=True, null=True)
    full_requester_name = models.CharField(max_length=255, blank=False, null=False)
    requester_mobile = PhoneNumberField(blank=False, null=False)
    # errands service
    pick_up_location = models.JSONField(default=dict, null=True, blank=True)
    drop_off_location = models.JSONField(default=dict, null=True, blank=True)
    destination = models.CharField(blank=True, null=True, max_length=255)
    # hotel service
    hotel_name = models.CharField(blank=True, null=True, max_length=255)
    check_in_date = models.DateField(null=True, blank=True)
    check_out_date = models.DateField(null=True, blank=True)
    number_of_rooms = models.IntegerField(null=True, blank=True)
    room_type = models.CharField(null=True, blank=True, max_length=55)
    number_of_adult = models.IntegerField(null=True, blank=True)
    number_of_children = models.IntegerField(null=True, blank=True)
    # travel tickets service
    flying_from = models.CharField(blank=True, null=True, max_length=125)
    flying_to = models.CharField(blank=True, null=True, max_length=125)
    departure_date = models.DateField(null=True, blank=True)
    returning_date = models.DateField(null=True, blank=True)
    number_of_adult_passengers = models.IntegerField(null=True, blank=True)
    number_of_children_passengers = models.IntegerField(null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.user.full_name}---->{self.service.name}'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        new = not bool(self.pk)
        if new and self.payment_method == self.CASH:
            self.payment_status = self.NOT_REQUIRED
        if not self.price and self.service.price:
            self.price = self.service.price
        if not self.price and not self.service.price:
            self.status = self.WAITING_PRICING
        if self.price and self.payment_status == self.NOT_REQUIRED:
            self.status = self.CREATED
        super(ServiceRequest, self).save(force_insert=False, force_update=False, using=None,
                                         update_fields=None)


@receiver(post_save, sender=ServiceRequest)
def my_handler(sender, **kwargs):
    old_object = ServiceRequest.objects.get(pk=kwargs['instance'].pk)
    old_status = old_object.status
    new_object = kwargs['instance']
    new_status = new_object.status
    from notifications.models import RequestNotificationSettings ,UserSavedNotifications

    notification=RequestNotificationSettings.objects.filter(previous_status=old_status,new_status=new_status)
    if notification:
        notification=notification.first()
        from fcm.utils import get_device_model
        Device = get_device_model()
        Device.objects.filter(user=new_object.user).send_message({'message': notification.message})
        UserSavedNotifications.objects.create(user=new_object.user,message=notification.message,redirect_obj=new_object.id,setting_id=notification.id)
