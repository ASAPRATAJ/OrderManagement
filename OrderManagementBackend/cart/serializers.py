import datetime

from rest_framework import serializers

from orders.models import Order, OrderProduct
from .models import Cart, CartItems
from products.serializers import ProductSerializer



class CartItemsSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()
    product = ProductSerializer(read_only=True)
    product_name = serializers.SlugRelatedField(
        source='product',
        read_only=True,
        slug_field='title'
    )

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Ilość produktu musi być większa niż 0.")
        return value

    class Meta:
        model = CartItems
        fields = ['id', 'product', 'product_id', 'quantity', 'product_name']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemsSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['id', 'items', 'created_at']


class CreateOrderFromCartSerializer(serializers.Serializer):
    delivery_date = serializers.DateField(required=True)  # Pole do pobierania daty dostawy

    def validate_delivery_date(self, value):
        # Pobieramy aktualną datę i godzinę
        today = datetime.date.today()
        current_time = datetime.datetime.now().time()
        noon = datetime.time(12, 0, 0)

        # Obliczamy najbliższy dostępny dzień dostawy
        if current_time > noon:
            today += datetime.timedelta(days=1) # Jeśli po 12:00, zamówienie przesuwa się o dzień

        # Szukamy pierwszego dostępnego dnia (wtorek-piątek)
        while today.weekday() not in [1, 2, 3, 4]:  # 1=Wtorek, 2=Środa, 3=Czwartek, 4=Piątek
            today += datetime.timedelta(days=1)

        # Sprawdzamy, czy wybrana data spełnia warunki
        if value < today:
            raise serializers.ValidationError(f"Delivery date must be selected between Tuesday and Friday.")

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
