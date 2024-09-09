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

    class Meta:
        model = Order
        fields = ['id', 'products', 'created_at']
        read_only_fields = ['created_at']

    def create(self, validated_data):
        products_data = validated_data.pop('orderproduct_set')

        user = self.context['request'].user

        order = Order.objects.create(user=user)
        for product_data in products_data:
            OrderProduct.objects.create(
                order=order,
                product=product_data['product'],
                quantity=product_data['quantity']
            )

        return order


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
        fields = ['id', 'created_at', 'user', 'products']
