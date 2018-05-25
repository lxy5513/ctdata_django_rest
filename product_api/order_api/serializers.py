#--*-- coding:utf-8 --*--
from rest_framework import serializers
from order_api.models import DeliveryOrder, ReceiverInfo, OrderLines 
from drf_writable_nested import WritableNestedModelSerializer


class OrderLinesSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderLines
        fields = ('id', 'itemCode', 'itemName', 'planQty', 'actualPrice', 'actualPrices')


class ReceiverInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiverInfo
        fields = ('id', 'name', 'mobile', 'province', 'city', 'area', 'detailAddress',)
        #read_only_fields = ('deliveryOrder')


class DeliveryOrderSerializer(WritableNestedModelSerializer):
    receiverInfo = ReceiverInfoSerializer(many=False) 
    orderLines = OrderLinesSerializer(many=True) 

    class Meta:
        model = DeliveryOrder
        fields = ('id', 'source', 'deliveryOrderCode', 'mainOrderId', 'actualPayPrice', 'mainCoupon', 'mainCurrency', 'mainCommission', 'channelName', 'shopNick', 'distributorNumber', 'storeHouse', 'supplier', 'orderType', 'createTime', 'totalAmount', 'buyerMessage', 'sellerMessage', 'remark', 'status', 'receiverInfo', 'orderLines')
