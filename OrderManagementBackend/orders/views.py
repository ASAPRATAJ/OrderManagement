from rest_framework import generics
from .serializers import OrderSerializer
from .models import Order


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
