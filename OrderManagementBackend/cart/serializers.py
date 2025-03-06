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
        if value < 4:
            raise serializers.ValidationError("Ilość produktu musi być większa niż 4.")
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

        # Warunek 1: Jeśli zamówienie jest po 12:00, nie można wybrać tego samego dnia
        if current_time > noon:
            if value == today:
                raise serializers.ValidationError("Nie można wybrać tego samego dnia, "
                                                  "jeśli zamówienie jest składane po godzinie 12:00.")

        # Warunek 2: Jeśli zamówienie jest po 12:00, nie można wybrać następnego dnia
        if current_time > noon:
            next_day = today + datetime.timedelta(days=1)
            if value == next_day:
                raise serializers.ValidationError("Nie można wybrać następnego dnia, "
                                                  "jeśli zamówienie jest składane po godzinie 12:00.")

        # Warunek 3: Jeśli zamówienie jest w czwartek po 12:00, piątek, sobota lub niedziela, najwcześniejszy dzień dostawy to wtorek
        if (today.weekday() == 3 and current_time > noon) or today.weekday() in [4, 5, 6]:  # 3=Czwartek, 4=Piątek, 5=Sobota, 6=Niedziela
            earliest_delivery = today
            while earliest_delivery.weekday() != 1:  # 1=Wtorek
                earliest_delivery += datetime.timedelta(days=1)
            if value < earliest_delivery:
                raise serializers.ValidationError(f"Składając zamówienie dzisiaj, najwcześniejszy dzień dostawy to {earliest_delivery.strftime('%Y-%m-%d')} (wtorek).")

        # Warunek 4: Użytkownik może wybrać termin odbioru tylko na wtorek/środę/czwartek/piątek
        if value.weekday() not in [1, 2, 3, 4]:  # 1=Wtorek, 2=Środa, 3=Czwartek, 4=Piątek
            raise serializers.ValidationError("Termin odbioru można wybrać tylko na wtorek, środę, czwartek lub piątek.")

        # Sprawdzenie, czy data dostawy nie jest w przeszłości
        if value < today:
            raise serializers.ValidationError("Data dostawy nie może być w przeszłości.")

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
