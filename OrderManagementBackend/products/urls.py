"""
URL configuration for the 'products' app.
Handles CRUD operations for products and product tags in the OrderManagement system.
"""

from django.urls import path
from .views import (
    ProductCreateView,
    ProductListView,
    ProductDetailView,
    ProductUpdateView,
    ProductDestroyView,
    ProductTagCreateView,
    ProductTagListView,
)

urlpatterns = [
    # Product endpoints
    path("", ProductListView.as_view(), name="product-list"),  # GET: List products
    path("create/", ProductCreateView.as_view(), name="product-create"),  # POST: Create product
    path("<int:pk>/", ProductDetailView.as_view(), name="product-detail"),  # GET: Product details
    path("<int:pk>/update/", ProductUpdateView.as_view(), name="product-update"),  # PUT/PATCH: Update product
    path("<int:pk>/delete/", ProductDestroyView.as_view(), name="product-delete"),  # DELETE: Delete product

    # Product tag endpoints
    path("tags/", ProductTagListView.as_view(), name="tag-list"),  # GET: List tags
    path("tags/create/", ProductTagCreateView.as_view(), name="tag-create"),  # POST: Create tag
]
