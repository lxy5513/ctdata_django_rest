from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles 


class ReceiverInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField('收货人姓名', max_length=255,)
    mobile = models.CharField('收货人手机号', max_length=255)
    province = models.CharField('地址省份', max_length=255, )
    city = models.CharField('地址城市', max_length=255, )
    area = models.CharField('区', max_length=255)
    detailAddress = models.CharField('详细地址', max_length=255, )
    
    class Meta:
        ordering = ('created',)


class OrderLines(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    itemCode = models.CharField('商品编号', max_length=255)
    itemName = models.CharField('商品名称', max_length=255)
    planQty = models.IntegerField('应发放商品数量', ) 
    actualPrice = models.FloatField('商品单价', )
    actualPrices = models.FloatField('商品总价', )

    class Meta:
        ordering = ('created',)


class DeliveryOrder(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    source = models.CharField('订单来源',max_length=100 )
    deliveryOrderCode = models.CharField('订单号',unique=True, max_length=100, help_text='1234567890')
    mainOrderId = models.CharField('母订单号', blank=True, max_length=100)
    actualPayPrice = models.FloatField('母单实际付款价格', blank=True, null=True)
    mainCoupon = models.FloatField('母单实际付款价格', blank=True, null=True)
    mainCurrency = models.FloatField('母订单芝蚂币', blank=True, null=True)
    mainCommission = models.FloatField('母订单佣金', blank=True, null=True)
    channelName = models.CharField('渠道名称', max_length=200, )
    shopNick = models.CharField('小店的名称', max_length=200, blank=True)
    distributorNumber = models.CharField('分销商编号', max_length=100, null=True, blank=True, help_text='12343213')
    storeHouse = models.BooleanField(max_length=1,default=0, choices=((0, '仓库直发'),(1, '一件代发'),), verbose_name='发货方式')
    supplier = models.CharField('供应商', max_length=200, blank=True)
    orderType = models.CharField('订单类型', max_length=10, blank=True, help_text='0开店订单，1店主订单，2三方订单')
    createTime = models.CharField('下单时间', max_length=100,)
    totalAmount = models.FloatField('订单总价', )
    buyerMessage = models.CharField('卖家留言', blank=True, max_length=400)
    sellerMessage = models.CharField('买家留言', blank=True, max_length=500)
    receiverInfo = models.ForeignKey(ReceiverInfo,null=True, blank=True, on_delete=models.CASCADE, related_name='receiverInfo')
    orderLines = models.ManyToManyField(OrderLines, null=True, blank=True)
    remark = models.CharField('备注', blank=True, max_length=500)
    status = models.CharField('订单状态',max_length=10)
    
    class Mate:
        ordering = ('created',)

    def __str__(self):
        return self.deliveryOrderCode 


