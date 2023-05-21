from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from service_requests.forms import RequestForm
from django.contrib import messages
from django.template.loader import render_to_string
from .filters import ServiceRequestFilter
from .models import ServiceRequest, GifteryCallback
# Create your views here.
from .permissions import GiftryPermission
from .serializers import ServiceRequestSerializer, ServiceRequestReadSerializer, GifteryCallbackSerializer


class ServiceRequestViewSets(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    serializer_class = ServiceRequestSerializer
    filterset_class = ServiceRequestFilter
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        return ServiceRequest.objects.filter(user=self.request.user)


    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ServiceRequestReadSerializer
        else:
            return ServiceRequestSerializer




class GifteryCallbackView(CreateAPIView,ListAPIView):
    serializer_class =GifteryCallbackSerializer

    def get_queryset(self):
        return GifteryCallback.objects.filter(user=self.request.user)

    def get_permissions(self):
        if self.request.method.lower() == 'get':
            return [IsAuthenticated()]
        else:
            return [GiftryPermission()]


def request_view(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            msg_html = render_to_string('service_requests/request_output.html', {'form': form})
            subject = 'New Request Form'
            message='Request Form Data'
            # message = f"Client Name: {form.cleaned_data['clientName']}\nPhone Number: {form.cleaned_data['phoneNumber']}\nAgent Name: {form.cleaned_data['AgentName']}\nType of Request Details: {form.cleaned_data['requestDetails']}\nDate and Time of Request: {form.cleaned_data['requestDateTime']}\nPickup Address: {form.cleaned_data['pickupAddress']}\nDrop-off Address: {form.cleaned_data['dropOffAddress']}\nNotes: {form.cleaned_data['notes']}"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = ["t.eltonsy@gmail.com"]
            send_mail(subject,message=message,from_email=from_email, recipient_list=recipient_list, html_message=msg_html,fail_silently=False)
            messages.success(request, 'Data submitted successfully!')
            form=RequestForm()
    else:
        form = RequestForm()
    return render(request, 'service_requests/request_form.html', {'form': form})

