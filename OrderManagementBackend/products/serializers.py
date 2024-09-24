from rest_framework import serializers
from .models import Product, ProductTag


class ProductTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTag
        fields = ['id', 'name']  # Serializacja tylko nazwy tagu


class ProductSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(queryset=ProductTag.objects.all(), many=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'image', 'tags']
