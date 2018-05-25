from django.contrib import admin
from .models import DeliveryOrder, OrderLines, ReceiverInfo

# Register your models here.

admin.site.register(DeliveryOrder)
admin.site.register(OrderLines)
admin.site.register(ReceiverInfo)
