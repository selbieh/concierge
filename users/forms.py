from django import forms
from django.conf import settings
from django.utils.encoding import force_str
from django.forms import ValidationError
from django.contrib.auth import  get_user_model
UserModel=get_user_model()
from django.contrib.auth.forms import SetPasswordForm, PasswordResetForm

class ResetPasswordForm(forms.Form):
    new_password1=forms.CharField()
    new_password2=forms.CharField()
    uid=forms.CharField(required=True)
    token=forms.CharField(required=True)

    set_password_form_class = SetPasswordForm

    _errors = {}
    user = None
    set_password_form = None

    def custom_validation(self, attrs):
        pass

    def clean(self):
        attrs=super().clean()
        print('atter',attrs)
        if 'allauth' in settings.INSTALLED_APPS:
            from allauth.account.forms import default_token_generator
            from allauth.account.utils import url_str_to_user_pk as uid_decoder
        else:
            from django.contrib.auth.tokens import default_token_generator
            from django.utils.http import urlsafe_base64_decode as uid_decoder

        # Decode the uidb64 (allauth use base36) to uid to get User object
        try:
            uid = force_str(uid_decoder(attrs['uid']))
            self.user = UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            raise ValidationError({'uid': ['Invalid value']})

        if not default_token_generator.check_token(self.user, attrs['token']):
            raise ValidationError({'token': ['Invalid value']})

        self.custom_validation(attrs)
        # Construct SetPasswordForm instance
        self.set_password_form = self.set_password_form_class(
            user=self.user, data=attrs,
        )
        if not self.set_password_form.is_valid():
            raise forms.ValidationError(self.set_password_form.errors)

        return attrs

    def save(self):
        return self.set_password_form.save()
