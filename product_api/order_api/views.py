from .models import DeliveryOrder, OrderLines, ReceiverInfo 
from .serializers import DeliveryOrderSerializer, OrderLinesSerializer, ReceiverInfoSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json


class DeliveryOrderList(APIView):
    """
    List all deliveryOrders, or create a new deliveryOrder.
    """
    def get(self, request, format=None):
        deliveryOrder = DeliveryOrder.objects.all()
        serializer = DeliveryOrderSerializer(deliveryOrder, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        order_data = request.data        
        order_data['source'] = 'xjdid'
        serializer = DeliveryOrderSerializer(data=order_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	


class DeliveryOrderDetail(APIView):
    """
    Retrieve, update or delete a deliveryOrder instance.
    """
    def get_object(self, pk):
        try:
            return DeliveryOrder.objects.get(pk=pk)
        except DeliveryOrder.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        deliveryOrder = self.get_object(pk)
        serializer = DeliveryOrderSerializer(deliveryOrder)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        deliveryOrder = self.get_object(pk)
        serializer = DeliveryOrderSerializer(deliveryOrder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        deliveryOrder = self.get_object(pk)
        deliveryOrder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class ReceiverInfoList(APIView):
    """
    List all receiverInfos, or create a new receiverInfo.
    """
    def get(self, request, format=None):
        receiverInfo = ReceiverInfo.objects.all()
        serializer = ReceiverInfoSerializer(receiverInfo, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReceiverInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	


class ReceiverInfoDetail(APIView):
    """
    Retrieve, update or delete a receiverInfo instance.
    """
    def get_object(self, pk):
        try:
            return ReceiverInfo.objects.get(pk=pk)
        except ReceiverInfo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        receiverInfo = self.get_object(pk)
        serializer = ReceiverInfoSerializer(receiverInfo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        receiverInfo = self.get_object(pk)
        serializer = ReceiverInfoSerializer(receiverInfo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        receiverInfo = self.get_object(pk)
        receiverInfo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class OrderLinesList(APIView):
    """
    List all orderLiness, or create a new orderLines.
    """
    def get(self, request, format=None):
        orderLines = OrderLines.objects.all()
        serializer = OrderLinesSerializer(orderLines, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderLinesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	


class OrderLinesDetail(APIView):
    """
    Retrieve, update or delete a orderLines instance.
    """
    def get_object(self, pk):
        try:
            return OrderLines.objects.get(pk=pk)
        except OrderLines.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        orderLines = self.get_object(pk)
        serializer = OrderLinesSerializer(orderLines)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        orderLines = self.get_object(pk)
        serializer = OrderLinesSerializer(orderLines, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        orderLines = self.get_object(pk)
        orderLines.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
