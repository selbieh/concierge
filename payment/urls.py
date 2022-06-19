from django.urls import path

from payment.views import PayOrder, OPayCallBack, opay_redirect_url

urlpatterns=[
    path('pay-order/<int:pk>/',PayOrder.as_view()),
    path('opay-callback/',OPayCallBack.as_view()),
    path('opay-redirect/',opay_redirect_url)
]