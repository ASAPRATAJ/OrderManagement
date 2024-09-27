from django.db import models
from users.models import CustomUser
from products.models import Product


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cart ID: {self.id}, created by: {self.user}'


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items', blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cartitems', blank=True, null=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.quantity} x {self.product}'


