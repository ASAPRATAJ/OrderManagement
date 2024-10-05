import datetime
from rest_framework import serializers
from .models import Order, OrderProduct
from products.models import Product


class OrderProductSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product')  # product_id do zapisu, powiązane z modelem Product

    class Meta:
        model = OrderProduct
        fields = ['product_id', 'quantity']  # product_id do zapisu, product do odczytu


class OrderCreateSerializer(serializers.ModelSerializer):
    products = OrderProductSerializer(source='orderproduct_set', many=True)
    delivery_date = serializers.DateField(required=True)  # Dodajemy pole delivery_date

    class Meta:
        model = Order
        fields = ['id', 'products', 'created_at', 'delivery_date']  # Upewnij się, że delivery_date jest tutaj
        read_only_fields = ['created_at']


class OrderProductListSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(source='product', read_only=True)
    product_title = serializers.CharField(source='product.title', read_only=True)  # Pobieramy nazwę produktu

    class Meta:
        model = OrderProduct
        fields = ['product_id', 'product_title', 'quantity']


class OrderListSerializer(serializers.ModelSerializer):
    products = OrderProductListSerializer(source='orderproduct_set', many=True)  # Używamy relacji do OrderProduct

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'user', 'delivery_date', 'products']
