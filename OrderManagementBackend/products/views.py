from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Product, ProductTag
from .serializers import ProductSerializer, ProductTagSerializer


class ProductCreateView(generics.CreateAPIView):
    """View for creating new Product object in database."""
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = ProductSerializer


class ProductListView(generics.ListAPIView):
    """View for listing existing Product objects in database."""
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    def get_queryset(self):
        """Changed list method with filtering Product object if Tag object exists in database."""

        queryset = Product.objects.all()
        tag = self.request.query_params.get('tag', None)
        if tag:
            queryset = queryset.filter(tags__name=tag)  # Filtrujemy produkty po tagu
        return queryset


class ProductDetailView(generics.RetrieveAPIView):
    """View for listing details of Product object from database."""
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer


class ProductUpdateView(generics.RetrieveUpdateAPIView):
    """View for updating specified Product object in database."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class ProductDestroyView(generics.DestroyAPIView):
    """View for deleting product object from database."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class ProductTagCreateView(generics.CreateAPIView):
    """View for creating Tag object in database."""
    queryset = ProductTag.objects.all()
    serializer_class = ProductTagSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class ProductTagListView(generics.ListAPIView):
    """View for listing Tag objects from database."""
    queryset = ProductTag.objects.all()
    serializer_class = ProductTagSerializer
    permission_classes = [IsAuthenticated]
