from rest_framework import generics
from .serializers import OrderCreateSerializer, OrderListSerializer
from .models import Order, OrderProduct


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
