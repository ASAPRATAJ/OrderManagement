from django.urls import path
from .views import OrderCreateView, OrderListView, UserOrderListView

urlpatterns = [
    path('orders/create/', OrderCreateView.as_view(), name='order-create'),
    path('orders/admin/', OrderListView.as_view(), name='order-list'),
    path('orders/', UserOrderListView.as_view(), name='user-orders'),

]
