from time import timezone

from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from orders.models import Order, OrderProduct
from products.models import Product
from .serializers import CartSerializer, CartItemsSerializer
from .models import Cart, CartItems


class CartDetailView(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Zwróć koszyk powiązany z zalogowanym użytkownikiem.
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        return cart


class CartItemListCreateView(generics.ListCreateAPIView):
    serializer_class = CartItemsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Pokaż tylko pozycje powiązane z koszykiem użytkownika
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        return CartItems.objects.filter(cart=cart)

    def perform_create(self, serializer):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        product_id = serializer.validated_data.get('product_id')  # Użyj product_id z serializer
        quantity = serializer.validated_data.get('quantity', 1)

        # Sprawdź, czy produkt istnieje
        product = get_object_or_404(Product, id=product_id)

        # Sprawdź, czy już istnieje wpis dla tego produktu w koszyku
        cart_item, created = CartItems.objects.get_or_create(cart=cart, product=product)

        if not created:
            # Jeśli już istnieje, zaktualizuj ilość
            cart_item.quantity += int(quantity)
        else:
            # Jeśli to nowy wpis, ustaw ilość
            cart_item.quantity = quantity

        cart_item.save()


class CartItemUpdateView(generics.UpdateAPIView):
    queryset = CartItems.objects.all()
    serializer_class = CartItemsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        return CartItems.objects.filter(cart=cart)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        new_quantity = request.data.get('quantity')

        if new_quantity is not None:
            if int(new_quantity) > 0:
                instance.quantity = new_quantity
                instance.save()
                return Response({'message': 'Quantity updated'}, status=status.HTTP_200_OK)
            else:
                # Jeśli ilość równa 0, usuń pozycję z koszyka
                instance.delete()
                return Response({'message': 'Item removed from cart'}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid quantity'}, status=status.HTTP_400_BAD_REQUEST)


class CartItemDeleteView(generics.DestroyAPIView):
    queryset = CartItems.objects.all()
    serializer_class = CartItemsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Usuń tylko pozycje z koszyka zalogowanego użytkownika
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        return CartItems.objects.filter(cart=cart)


class CreateOrderFromCartView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Pobierz koszyk użytkownika
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_items = CartItems.objects.filter(cart=cart)

        if not cart_items.exists():
            return Response({'error': 'Koszyk jest pusty'}, status=status.HTTP_400_BAD_REQUEST)

        # Stwórz zamówienie
        order = Order.objects.create(user=request.user)

        # Dodaj produkty z koszyka do zamówienia
        for item in cart_items:
            OrderProduct.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity
            )

        # Wyczyść koszyk
        cart_items.delete()

        return Response({'message': 'Zamówienie zostało utworzone', 'order_id': order.id}, status=status.HTTP_201_CREATED)
