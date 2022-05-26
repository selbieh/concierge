# Create your views here.
import uuid
from django.conf import settings
import requests
from rest_framework import serializers
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from service_requests.models import ServiceRequest
from service_requests.serializers import ServiceRequestSerializer


def prepare_payment_json(service_order: ServiceRequest) -> dict:
    new_identifier = f'{service_order.id}-u-{str(uuid.uuid4())}'
    service_order.payment_unique_ident=new_identifier
    service_order.payment_unique_ident_history=service_order.payment_unique_ident_history or []+[new_identifier]
    service_order.save()
    return {
        "country": "EG",
        "reference": service_order.payment_unique_ident,
        "amount": {
            "total": 400,
            "currency": "EGP"
        },
        "returnUrl": "https://your-return-url",
        "callbackUrl": "https://your-call-back-url",
        "cancelUrl": "https://your-cacel-url",
        "expireAt": 300,
        "userInfo": {
            "userEmail": service_order.user.email,
            "userId": service_order.user.id,
            "userMobile": service_order.user.mobile,
            "userName": service_order.user.full_name
        },
        "productList": [
            {
                "productId": "productId",
                "name": "name",
                "description": "description",
                "price": 100,
                "quantity": 2,
                "imageUrl": "https://imageUrl.com"
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
        headers = {"Authorization":f"Bearer {settings.PUBLIC_KEY}","MerchantId":f"{settings.MERCHANT_ID}"}
        response=requests.post(settings.PAYMENT_URL,json=payload,headers=headers)
        return Response(response.json())
