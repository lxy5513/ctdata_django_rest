#--*-- coding:utf-8 --*--
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from order_api import views

urlpatterns = [
    url(r'^deliveryOrders/$', views.DeliveryOrderList.as_view()),
    url(r'^deliveryOrders/(?P<pk>[0-9]+)/$', views.OrderLinesDetail.as_view()),
    url(r'^orderLiness/$', views.OrderLinesList.as_view()),
    url(r'^orderLiness/(?P<pk>[0-9]+)/$', views.OrderLinesDetail.as_view()),
    url(r'^receiverInfos/$', views.ReceiverInfoList.as_view()),
    url(r'^receiverInfos/(?P<pk>[0-9]+)/$', views.ReceiverInfoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
