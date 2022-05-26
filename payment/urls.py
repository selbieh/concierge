from django.urls import path

from payment.views import PayOrder

urlpatterns=[
    path('pay-order/<int:pk>/',PayOrder.as_view())
]