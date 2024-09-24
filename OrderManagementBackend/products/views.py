from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Product, ProductTag
from .serializers import ProductSerializer, ProductTagSerializer


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = ProductSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    def get_queryset(self):
        """
        Opcjonalnie filtrujemy produkty po tagu, jeśli 'tag' jest obecny w parametrze zapytania
        """
        queryset = Product.objects.all()
        tag = self.request.query_params.get('tag', None)
        if tag:
            queryset = queryset.filter(tags__name=tag)  # Filtrujemy produkty po tagu
        return queryset


class ProductDetailView(generics.RetrieveAPIView):
    """
    Widok do wyświetlania szczegółów konkretnego produktu.
    """
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer


class ProductUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class ProductDestroyView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class ProductTagCreateView(generics.CreateAPIView):
    queryset = ProductTag.objects.all()
    serializer_class = ProductTagSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class ProductTagListView(generics.ListAPIView):
    queryset = ProductTag.objects.all()
    serializer_class = ProductTagSerializer
    permission_classes = [IsAuthenticated]
