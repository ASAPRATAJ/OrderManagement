"""
Views for the 'products' app.
Handles CRUD operations for products and tags with role-based access control.
"""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Product, ProductTag
from .serializers import ProductSerializer, ProductTagSerializer


class ProductListView(generics.ListAPIView):
    """List products with optional tag filtering (accessible to all authenticated users)."""
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    def get_queryset(self):
        """Return queryset based on user role and query parameters."""
        if self.request.user.is_staff:
            queryset = Product.objects.all()  # Admins see all products
        else:
            queryset = Product.objects.filter(is_active=True)  # Regular users see only active products

        # Filter by tag if provided
        tag = self.request.query_params.get("tag")
        if tag:
            queryset = queryset.filter(tags__name=tag)

        return queryset


class ProductCreateView(generics.CreateAPIView):
    """Create a new product (admin only)."""
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    """Retrieve details of a specific product (accessible to all authenticated users)."""
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer


class ProductUpdateView(generics.UpdateAPIView):
    """Update an existing product (admin only)."""
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = ProductSerializer


class ProductDestroyView(generics.DestroyAPIView):
    """Delete a product (admin only)."""
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = ProductSerializer


class ProductTagListView(generics.ListAPIView):
    """List all product tags (accessible to all authenticated users)."""
    queryset = ProductTag.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProductTagSerializer


class ProductTagCreateView(generics.CreateAPIView):
    """Create a new product tag (admin only)."""
    queryset = ProductTag.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = ProductTagSerializer
