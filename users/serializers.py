from allauth.account import adapter
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from dj_rest_auth.registration.serializers import RegisterSerializer
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from customers.models import InvitationCode
from django.core.exceptions import ValidationError as DjangoValidationError

from customers.serializers import CustomerSerializer
from users.models import User


class CustomRegisterSerializer(RegisterSerializer):
    username = serializers.CharField(allow_null=True, allow_blank=True, required=False)
    mobile = PhoneNumberField(allow_null=False, validators=[UniqueValidator(queryset=User.objects.all())])
    dob = serializers.DateField(allow_null=True, required=False)
    avatar = serializers.FileField(allow_null=True, required=False)
    full_name = serializers.CharField()
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    invitation_code = serializers.CharField(allow_null=False)

    def validate_invitation_code(self, invitation_code):
        try:
            InvitationCode.objects.get(code=invitation_code, used=False)
        except:
            raise serializers.ValidationError("invalid invitation code or used befor")
        return invitation_code

    def get_cleaned_data(self):
        invitation_code_obj = InvitationCode.objects.get(code=self.validated_data.get('invitation_code', ''))
        data = {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'mobile': self.validated_data.get('mobile', ''),
            'full_name': self.validated_data.get('full_name', ''),
            "invitation_code": invitation_code_obj,
            "customer": invitation_code_obj.customer,

        }
        return data

    def save(self, request):
        cleaned_data = self.get_cleaned_data()
        password = cleaned_data.pop('password1')
        user = User(**cleaned_data)
        user.set_password(password)
        user.save()
        invitation_code = user.invitation_code
        invitation_code.used = True
        invitation_code.save()
        user.save()
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user


class ReadUserDataSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    mobile = PhoneNumberField()
    dob = serializers.DateField()
    avatar = serializers.FileField()
    full_name = serializers.CharField()
    email = serializers.EmailField()
    invitation_code = serializers.CharField(source="invitation_code.code",default=None)
    customer = CustomerSerializer(many=False)


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['mobile', 'avatar', 'full_name', 'dob']