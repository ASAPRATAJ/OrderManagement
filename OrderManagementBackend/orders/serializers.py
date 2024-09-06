from rest_framework import serializers
from .models import Order
from users.serializers import ListCustomUserSerializer
from products.serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'user', 'created_at', 'products']



class ListOrderSerializer(serializers.ModelSerializer):
    user = ListCustomUserSerializer(read_only=True)  # Zwraca dane o użytkowniku
    products = ProductSerializer(many=True, read_only=True)  # Zwraca listę produktów

    class Meta:
        model = Order
        fields = '__all__'
