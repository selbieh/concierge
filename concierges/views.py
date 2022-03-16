import requests
from allauth.account import app_settings
from django.core import signing
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, render

from users.forms import ResetPasswordForm
from users.models import User


def custom_confirm(request, key):

    response = requests.post(request.build_absolute_uri(reverse('rest_verify_email')), data={"key": key})
    if response.status_code == 200:
        msg = 'mail confirmed'
    else:
        msg = 'link not found'
    return HttpResponse(msg)




def custom_reset_handler(request,uid,token):
    return render(request,'rest_password_form.html',context={"uid":uid,"token":token})

def custom_reset_handler_submit(request):
    print(request.POST)
    form=ResetPasswordForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse('password changed')
    else:
        errors=form.errors
        return render(request, 'rest_password_form.html', context={"errors":errors,"uid": request.POST['uid'], "token": request.POST['token']})
