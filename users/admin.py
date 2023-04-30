from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group, Permission
from phonenumber_field.formfields import PhoneNumberField
from .models import User

class UserCreationModelForm(UserCreationForm):
    email = forms.EmailField(required=True)
    mobile = PhoneNumberField(required=True)
    full_name = forms.CharField(max_length=55, required=True)
    dob = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date'}))
    avatar = forms.FileField(required=False)
    is_active = forms.BooleanField(required=False)
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), required=False)
    user_permissions = forms.ModelMultipleChoiceField(queryset=Permission.objects.all(), required=False)

    class Meta:
        model = User
        fields = ('email', 'mobile', 'full_name', 'dob', 'avatar', 'password1', 'password2', 'is_active',  'groups', 'user_permissions')

    def save(self, commit=True):
        user = super(UserCreationModelForm, self).save(commit=False)
        user.password = make_password(self.cleaned_data['password1'])
        if commit:
            user.save()
            # Add user to groups
            group_ids = self.cleaned_data.get('groups', [])
            for group_id in group_ids:
                group = Group.objects.get(pk=group_id)
                user.groups.add(group)
            # Add user permissions
            permission_ids = self.cleaned_data.get('user_permissions', [])
            permissions = Permission.objects.filter(pk__in=permission_ids)
            user.user_permissions.set(permissions)
        return user
class CustomUserAdmin(UserAdmin):
    add_form = UserCreationModelForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'full_name', 'mobile', 'dob', 'avatar', 'is_active','groups', 'user_permissions')}
        ),
    )

    # other admin options...
