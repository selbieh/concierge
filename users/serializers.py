from dj_rest_auth.registration.serializers import RegisterSerializer
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework.validators import UniqueValidator
from rest_framework import serializers

from users.models import User


class CustomRegisterSerializer(RegisterSerializer):
    username = serializers.CharField(allow_null=True,allow_blank=True,required=False)
    mobile=PhoneNumberField(allow_null=False,validators=[UniqueValidator(queryset=User.objects.all())])
    dob =serializers.DateField(allow_null=True,required=False)
    avatar=serializers.FileField(allow_null=True,required=False)
    full_name=serializers.CharField()
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    invitation_code=serializers.CharField(allow_null=False)
