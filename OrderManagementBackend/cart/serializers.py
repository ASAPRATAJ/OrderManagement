from rest_framework import serializers

from orders.models import Order, OrderProduct
from .models import Cart, CartItems
from products.serializers import ProductSerializer
import datetime


class CartItemsSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItems
        fields = ['id', 'product', 'product_id', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemsSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['id', 'items', 'created_at']


class CreateOrderFromCartSerializer(serializers.Serializer):
    delivery_date = serializers.DateField(required=True)  # Pole do pobierania daty dostawy

    def validate_delivery_date(self, value): # noqa
        # Pobieramy aktualną datę i godzinę
        today = datetime.date.today()
        current_time = datetime.datetime.now().time()

        # Sprawdzenie czy jest przed czy po godzinie 12:00
        noon = datetime.time(12, 0, 0)

        # Jeśli zamówienie jest złożone po godzinie 12:00
        if current_time > noon:
            # Sprawdź, czy wybrano datę na pojutrze lub później
            if value <= today + datetime.timedelta(days=1):
                raise serializers.ValidationError("If order is placed after 12:00 PM, "
                                                  "the earliest delivery date is the day after tomorrow.")
        else:
            # Jeśli zamówienie złożone przed 12:00, sprawdzamy, czy data jest co najmniej jutrzejsza
            if value <= today:
                raise serializers.ValidationError("Delivery date must be at least tomorrow's date.")
        return value

    def create(self, validated_data):
        user = self.context['request'].user
        delivery_date = validated_data['delivery_date']

        # Pobierz koszyk użytkownika
        cart, _ = Cart.objects.get_or_create(user=user)
        cart_items = CartItems.objects.filter(cart=cart)

        if not cart_items.exists():
            raise serializers.ValidationError("Koszyk jest pusty")

        # Stwórz zamówienie z delivery_date
        order = Order.objects.create(user=user, delivery_date=delivery_date)

        # Dodaj produkty z koszyka do zamówienia
        for item in cart_items:
            OrderProduct.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity
            )

        # Wyczyść koszyk
        cart_items.delete()

        return order
