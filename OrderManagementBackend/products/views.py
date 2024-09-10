from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Product
from .serializers import ProductSerializer


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = ProductSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

