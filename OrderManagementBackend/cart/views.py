from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from products.models import Product
from .serializers import CartSerializer, CartItemsSerializer, CreateOrderFromCartSerializer
from .models import Cart, CartItems


class CartDetailView(generics.RetrieveAPIView):
    """View for listing details of Cart object from database."""
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """Return cart related to requesting user."""
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        return cart


class CartItemListCreateView(generics.ListCreateAPIView):
    """View for listing related Cart or creating Cart object if doesn't exist in database."""
    serializer_class = CartItemsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Show only items related to user's Cart."""
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        return CartItems.objects.filter(cart=cart)

    def perform_create(self, serializer):
        """Create new Cart if doesn't exist and then add new item."""
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        product_id = serializer.validated_data.get('product_id')
        quantity = serializer.validated_data.get('quantity', 1)

        product = get_object_or_404(Product, id=product_id)

        cart_item, created = CartItems.objects.get_or_create(cart=cart, product=product)

        if not created:
            cart_item.quantity += int(quantity)
        else:
            cart_item.quantity = quantity

        cart_item.save()


class CartItemUpdateView(generics.UpdateAPIView):
    """View for updating quantities of products in Cart."""
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
    """View for deleting Product from Cart."""
    queryset = CartItems.objects.all()
    serializer_class = CartItemsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Usuń tylko pozycje z koszyka zalogowanego użytkownika
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        return CartItems.objects.filter(cart=cart)


class CreateOrderFromCartView(generics.GenericAPIView):
    """View for changing Cart to Order."""
    permission_classes = [IsAuthenticated]
    serializer_class = CreateOrderFromCartSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Utwórz zamówienie
            order = serializer.save()

            return Response({'message': 'Zamówienie zostało utworzone', 'order_id': order.id},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
