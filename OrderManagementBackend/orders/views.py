from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import OrderCreateSerializer, OrderListSerializer
from .models import Order


class OrderCreateView(generics.CreateAPIView):
    """View for creating Order object in database."""
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        """Overridden method to stick user with Order."""
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class OrderListView(generics.ListAPIView):
    """View for listing orders from database."""
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        """Overridden method for listing to show latest orders on the top."""
        return Order.objects.all().order_by('-created_at')


class UserOrderListView(generics.ListAPIView):
    """View for list all users from database."""
    serializer_class = OrderListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Overridden method for listing to filter listing users by permissions granted."""
        if self.request.user.is_staff is True:
            return Order.objects.all().order_by('-created_at')
        return Order.objects.filter(user=self.request.user).order_by('-created_at')

