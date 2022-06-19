from django.urls import path

from payment.views import PayOrder, OPayCallBack

urlpatterns=[
    path('pay-order/<int:pk>/',PayOrder.as_view()),
    path('opay-callback/',OPayCallBack.as_view())
]