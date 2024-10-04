from rest_framework import serializers
from .models import Cart, CartItems
from products.serializers import ProductSerializer


class CartItemsSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(write_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItems
        fields = ['id', 'product', 'product_id', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemsSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['id', 'items', 'created_at']
