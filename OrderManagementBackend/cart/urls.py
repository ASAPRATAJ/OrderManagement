from django.urls import path
from .views import CartDetailView, CartItemListCreateView, CartItemUpdateView, CartItemDeleteView, CreateOrderFromCartView

urlpatterns = [
    path('cart/', CartDetailView.as_view(), name='cart-detail'),
    path('cart/items/', CartItemListCreateView.as_view(), name='cart-items'),
    path('cart/items/<int:pk>/', CartItemUpdateView.as_view(), name='cart-item-update'),
    path('cart/items/<int:pk>/delete/', CartItemDeleteView.as_view(), name='cart-item-delete'),
    path('cart/create-order/', CreateOrderFromCartView.as_view(), name='create-order'),
]
