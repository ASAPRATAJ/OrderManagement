from django.urls import path
from .views import (ProductCreateView,
                    ProductListView,
                    ProductImageUpdateView,
                    ProductDestroyView,
                    ProductTagCreateView,
                    ProductTagListView)

urlpatterns = [
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/update-image/', ProductImageUpdateView.as_view(), name='product-update-image'),
    path('products/<int:pk>/delete/', ProductDestroyView.as_view(), name='product-delete'),
    path('products/tags/create/', ProductTagCreateView.as_view(), name='tag-create'),
    path('products/tags/', ProductTagListView.as_view(), name='tag-create'),
]
