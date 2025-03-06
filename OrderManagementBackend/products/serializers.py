"""
Serializers for the 'products' app.
Handles serialization and deserialization of Product and ProductTag models.
"""

from rest_framework import serializers

from .models import Product, ProductTag


class ProductTagSerializer(serializers.ModelSerializer):
    """Serializer for ProductTag model, exposing ID and name."""

    class Meta:
        model = ProductTag
        fields = ["id", "name"]


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product model, including nested tags."""
    tags = ProductTagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=ProductTag.objects.all(),
        many=True,
        write_only=True,
        source="tags",
    )

    class Meta:
        model = Product
        fields = ["id", "title", "description", "price", "image", "tags", "tag_ids", "is_active"]

    def validate_price(self, value):
        """Ensure price is positive."""
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value
