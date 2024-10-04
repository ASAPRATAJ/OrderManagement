from django.urls import path
from .views import (ProductCreateView,
                    ProductListView,
                    ProductDetailView,
                    ProductUpdateView,
                    ProductDestroyView,
                    ProductTagCreateView,
                    ProductTagListView)

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', ProductDestroyView.as_view(), name='product-delete'),
    path('products/tags/create/', ProductTagCreateView.as_view(), name='tag-create'),
    path('products/tags/', ProductTagListView.as_view(), name='tag-list'),
]
