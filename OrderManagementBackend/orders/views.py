from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import OrderCreateSerializer, OrderListSerializer
from .models import Order


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        return Order.objects.all().order_by('-created_at')


class UserOrderListView(generics.ListAPIView):
    serializer_class = OrderListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff is True:
            return Order.objects.all().order_by('-created_at')
        return Order.objects.filter(user=self.request.user).order_by('-created_at')

