from django.urls import path
from .views import (CartDetailView,
                    CartItemListCreateView,
                    CartItemUpdateView,
                    CartItemDeleteView,
                    CreateOrderFromCartView)

urlpatterns = [
    path("", CartDetailView.as_view(), name='cart-detail'),
    path("items/", CartItemListCreateView.as_view(), name='cart-items'),
    path("items/<int:pk>/", CartItemUpdateView.as_view(), name='cart-item-update'),
    path("items/<int:pk>/delete/", CartItemDeleteView.as_view(), name='cart-item-delete'),
    path("create-order/", CreateOrderFromCartView.as_view(), name='create-order'),
]
