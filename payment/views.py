# Create your views here.
import uuid

import pr as pr
from django.conf import settings
import requests
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from payment.models import PayOrderResponseLog
from service_requests.models import ServiceRequest
from service_requests.serializers import ServiceRequestSerializer


def prepare_payment_json(service_order: ServiceRequest) -> dict:
    new_identifier = f'{service_order.id}-u-{str(uuid.uuid4())}'
    service_order.payment_unique_ident=new_identifier
    old_ident_list=service_order.payment_unique_ident_history or []
    old_ident_list.append(new_identifier)
    service_order.payment_unique_ident_history=old_ident_list
    service_order.save()
    return {
        "country": "EG",
        "reference": service_order.payment_unique_ident,
        "amount": {
            "total": service_order.price *100,
            "currency": "EGP"
        },
        "returnUrl": f"{settings.OPAY_REDIRECT_URL}",
        "callbackUrl": f"{settings.OPAY_CALLBACK_URL}",
        "cancelUrl": f"{settings.SERVER_DOMAIN}/payment/call-back/",
        "expireAt": 300,
        "userInfo": {
            "userEmail": service_order.user.email,
            "userId": service_order.user.id,
            "userMobile": str(service_order.user.mobile),
            "userName": service_order.user.full_name
        },
        "productList": [
            {
                "productId": service_order.service.id if service_order.service else '',
                "name": service_order.service.name if service_order.service else '',
                "description": service_order.service.description if service_order.service else '',
                "price": service_order.price,
                "quantity": 1,
                "imageUrl": f"{service_order.service.image.url or ''}"
            }
        ],
    }



def validate_order_payable(service_order:ServiceRequest)->bool:
    if not service_order.payment_method ==ServiceRequest.CARD:
        raise serializers.ValidationError(detail='payment method must be online payable')
    if service_order.payment_status == 'paid':
        raise serializers.ValidationError(detail='cannot pay already paid order')
    if service_order.price ==None:
        raise serializers.ValidationError(detail='cannot pay waiting for price order')


class PayOrder(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ServiceRequestSerializer

    def get_queryset(self):
        return ServiceRequest.objects.filter(user=self.request.user)


    def retrieve(self, request, *args, **kwargs):
        service_order=self.get_object()
        validate_order_payable(service_order)
        payload=prepare_payment_json(service_order)
        header = {"Authorization":f"Bearer {settings.PAYMENT_PUBLIC_KEY}","MerchantId":f"{settings.PAYMENT_MERCHANT_ID}"}
        response=requests.post(settings.PAYMENT_URL,json=payload,headers=header)
        PayOrderResponseLog.objects.create(opay_response=response.json(),order=service_order,reference=service_order.payment_unique_ident)
        return Response(response.json())


class OPayCallBack(APIView):
    permission_classes = []

    def post(self,request):
        reference = request.data['payload']['reference']

        if request.META['HTTP_HOST'] == "api.opaycheckout.com" :
            payment_log_obj=get_object_or_404(PayOrderResponseLog,reference=reference)
            payment_log_obj.callback=request.data
            payment_log_obj.save()
            order=payment_log_obj.order
            if request.data.get('status') == "SUCCESS":
                order.payment_status='paid'
                order.save()
            return Response("call back saved")
        else:
            payment_log_obj = get_object_or_404(PayOrderResponseLog, reference=reference)
            payment_log_obj.callback = request.data
            payment_log_obj.false_ip_callback=True
            payment_log_obj.save()
            return Response("invalid ip")


def opay_redirect_url(request):
    print(vars(request))
    return HttpResponse("payment placed and we will inform you with th payment status")
