from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    mobile = PhoneNumberField(required=True)
    full_name = forms.CharField(max_length=55, required=True)
    dob = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date'}))
    avatar = forms.FileField(required=False)

    class Meta:
        model = User
        fields = ( 'email', 'mobile', 'full_name', 'dob', 'avatar', 'password1', 'password2')
        
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm

admin.site.register(User, CustomUserAdmin)

