from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderCreateSerializer, OrderListSerializer
from .models import Order


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = [IsAuthenticated]


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    permission_classes = [IsAuthenticated]
