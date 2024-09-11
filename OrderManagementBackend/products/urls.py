from django.urls import path
from .views import ProductCreateView, ProductListView, ProductDetailView, ProductImageUpdateView

urlpatterns = [
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/<int:pk>/update-image/', ProductImageUpdateView.as_view(), name='product-update-image'),
]
