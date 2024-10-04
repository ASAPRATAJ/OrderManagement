from rest_framework import serializers
from .models import Product, ProductTag


class ProductTagSerializer(serializers.ModelSerializer):
    """Serializer for ProductTag Model."""
    class Meta:
        model = ProductTag
        fields = ['id', 'name']  # It will serialize and deserialize ID and NAME fields from/to database


class ProductSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(queryset=ProductTag.objects.all(), many=True)
    # it adds tag field from ProductTag model while serialize Product

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'image', 'tags']
