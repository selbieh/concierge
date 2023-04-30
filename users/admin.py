from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from phonenumber_field.formfields import PhoneNumberField
from .models import User
from django import forms

class UserCreationModelForm(UserCreationForm):
    email = forms.EmailField(required=True)
    mobile = PhoneNumberField(required=True)
    full_name = forms.CharField(max_length=55, required=True)
    dob = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date'}))
    avatar = forms.FileField(required=False)

    class Meta:
        model = User
        fields = ('email', 'mobile', 'full_name', 'dob', 'avatar', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserCreationModelForm, self).save(commit=False)
        user.password = make_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationModelForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'full_name', 'mobile', 'dob', 'avatar')}
        ),
    )

admin.site.register(User, CustomUserAdmin)
