from rest_framework import serializers

from .models import Order, OrderProduct
from products.models import Product


class OrderProductSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product')

    class Meta:
        model = OrderProduct
        fields = ['product_id', 'quantity']


class OrderCreateSerializer(serializers.ModelSerializer):
    products = OrderProductSerializer(source='orderproduct_set', many=True)
    delivery_date = serializers.DateField(required=True)

    class Meta:
        model = Order
        fields = ['id', 'products', 'created_at', 'delivery_date']
        read_only_fields = ['created_at']


class OrderProductListSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(source='product', read_only=True)
    product_title = serializers.CharField(source='product.title', read_only=True)

    class Meta:
        model = OrderProduct
        fields = ['product_id', 'product_title', 'quantity']


class OrderListSerializer(serializers.ModelSerializer):
    products = OrderProductListSerializer(source='orderproduct_set', many=True)
    company_name = serializers.CharField(source='user.company_name', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'user', 'delivery_date', 'products', 'company_name']
