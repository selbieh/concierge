from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from openpyxl.styles.builtins import total
from phonenumber_field.modelfields import PhoneNumberField
from pyasn1.compat.octets import null

status_map={
    #[new or old,  status , paymen_method ,payment_status ,price]--->[status,payment_status]
    (True,'created','cash'):('created','not required'),
    (True,'created','card'):('waiting payment',None)
}


def upload_image(instance, filename):
    return "service_request/{0}/{1}".format(instance.id, filename)

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
        (WAITING_PRICING,WAITING_PRICING)
    ]
    payment_methods_choices = [
        (CASH, CASH),
        (CARD, CARD)
    ]
    payment_unique_ident=models.CharField(max_length=125,blank=True,null=True)
    payment_unique_ident_history=ArrayField(models.CharField(max_length=125), blank=True,null=True)
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
    document_file=models.FileField(upload_to=upload_image,blank=True,null=True)
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
    # number_of_adult_passengers = models.IntegerField(null=True, blank=True)
    # number_of_children_passengers = models.IntegerField(null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    doctor_name = models.CharField(max_length=125,null=True,blank=True)
    hospital_or_clinic_address =models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return f'{self.user.full_name}---->{self.service.name}'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        new = not bool(self.pk)
        if status_map.get((new,self.status,self.payment_method)):
            self.status,self.payment_status=status_map.get((new,self.status,self.payment_method))
        if not self.price and self.service.price:
            self.price = self.service.price
        if not self.price and not self.service.price:
            self.status = self.WAITING_PRICING
        super(ServiceRequest, self).save(force_insert=False, force_update=False, using=None,
                                          update_fields=None)
                                # if new and self.payment_method == self.CASH and self.status==self.CREATED:
                                #     self.payment_status = self.NOT_REQUIRED


                                # if self.price and self.payment_status == self.NOT_REQUIRED:
                                #     self.status = self.CREATED
                                # if self.payment_method == self.CARD:
                                #     print(self.payment_status)
                                #     self.payment_status=self.WAITING_PAYMENT
                                #     print(self.payment_status)



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
        from firebase_admin.messaging import Message, Notification
        from fcm_django.models import FCMDevice
        message = Message(
            notification=Notification(title="", body=notification.message, image="")
            # topic="notification",
        )
        FCMDevice.objects.filter(user=new_object.user).send_message(message)
        UserSavedNotifications.objects.create(user=new_object.user,message=notification.message,redirect_obj=new_object.id,setting_id=notification.id)



class GifteryCallback(models.Model):
    user = models.ForeignKey('users.User',blank=False,null=False,on_delete=models.PROTECT)
    total_price = models.FloatField()
    product_list=ArrayField(models.JSONField(default=dict),blank=False,null=False)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    giftry_order_id=models.CharField(max_length=125,blank=False,null=False)
