
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

def upload_avatar(instance, filename):
    return "users/{0}/{1}".format(instance.id, filename)

class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=False,
        blank=True,
        null=True

    )
    email = models.EmailField(blank=False,null=False,unique=True)
    mobile=PhoneNumberField(blank=False,null=False)
    full_name=models.CharField(max_length=55,blank=False,null=False)
    dob=models.DateField(blank=True,null=True)
    avatar=models.FileField(upload_to=upload_avatar,blank=True,null=True)
    invitation_Code=models.ForeignKey('customers.InvitationCode',null=True,blank=True,on_delete=models.PROTECT)
    customer=models.ForeignKey('customers.Customer',null=True,blank=True,on_delete=models.PROTECT)
    is_active = models.BooleanField(
        default=True,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    mail_confirmed=models.BooleanField(default=False)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=['username','full_name','mobile']
