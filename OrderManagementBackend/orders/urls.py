"""
URL configuration for the 'orders' app.
Handles order creation and retrieval for users and administrators.
"""

from django.urls import path
from .views import (
    OrderCreateView,
    # OrderListView,
    UserOrderListView,
)

urlpatterns = [
    # Order creation
    path("create/", OrderCreateView.as_view(), name="order-create"),  # POST: Create order

    # Order listing for administrators
    # path("admin/", OrderListView.as_view(), name="admin-order-list"),  # GET: List orders (admin only)

    # Order listing for users
    path("", UserOrderListView.as_view(), name="order-list"),  # GET: List user's orders (requested user),
                                                               #      List all orders (admin only)
]
