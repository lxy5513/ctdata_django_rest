# Generated by Django 2.0.4 on 2018-05-24 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('source', models.CharField(max_length=100, verbose_name='订单来源')),
                ('deliveryOrderCode', models.CharField(help_text='1234567890', max_length=100, unique=True, verbose_name='订单号')),
                ('mainOrderId', models.CharField(blank=True, max_length=100, verbose_name='母订单号')),
                ('actualPayPrice', models.FloatField(blank=True, null=True, verbose_name='母单实际付款价格')),
                ('mainCoupon', models.FloatField(blank=True, null=True, verbose_name='母单实际付款价格')),
                ('mainCurrency', models.FloatField(blank=True, null=True, verbose_name='母订单芝蚂币')),
                ('mainCommission', models.FloatField(blank=True, null=True, verbose_name='母订单佣金')),
                ('channelName', models.CharField(max_length=200, verbose_name='渠道名称')),
                ('shopNick', models.CharField(blank=True, max_length=200, verbose_name='小店的名称')),
                ('distributorNumber', models.CharField(help_text='12343213', max_length=100, verbose_name='分销商编号')),
                ('storeHouse', models.BooleanField(choices=[(0, '仓库直发'), (1, '一件代发')], default=0, max_length=1, verbose_name='发货方式')),
                ('supplier', models.CharField(blank=True, max_length=200, verbose_name='供应商')),
                ('orderType', models.CharField(blank=True, help_text='0开店订单，1店主订单，2三方订单', max_length=10, verbose_name='订单类型')),
                ('createTime', models.CharField(max_length=100, verbose_name='下单时间')),
                ('totalAmount', models.FloatField(verbose_name='订单总价')),
                ('buyerMessage', models.CharField(blank=True, max_length=400, verbose_name='卖家留言')),
                ('sellerMessage', models.CharField(blank=True, max_length=500, verbose_name='买家留言')),
                ('remark', models.CharField(blank=True, max_length=500, verbose_name='备注')),
                ('status', models.CharField(max_length=10, verbose_name='订单状态')),
            ],
        ),
        migrations.CreateModel(
            name='OrderLines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('itemCode', models.CharField(max_length=50, verbose_name='商品编号')),
                ('itemName', models.CharField(max_length=50, verbose_name='商品名称')),
                ('planQty', models.IntegerField(verbose_name='应发放商品数量')),
                ('actualPrice', models.FloatField(verbose_name='商品单价')),
                ('actualPrices', models.FloatField(verbose_name='商品总价')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='ReceiverInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50, verbose_name='收货人姓名')),
                ('mobile', models.CharField(max_length=20, verbose_name='收货人手机号')),
                ('province', models.CharField(max_length=50, verbose_name='地址省份')),
                ('city', models.CharField(max_length=50, verbose_name='地址城市')),
                ('area', models.CharField(max_length=50, verbose_name='区')),
                ('detailAddress', models.CharField(max_length=50, verbose_name='详细地址')),
                ('deliveryOrder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiverInfo', to='order_api.DeliveryOrder')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
