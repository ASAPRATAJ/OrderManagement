from django.db import models
from users.models import CustomUser
from products.models import Product


class Order(models.Model):
    """Fields of Order Model in database."""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderProduct')
    created_at = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Order ID{self.id}, created by {self.user}"


class OrderProduct(models.Model):
    """Through model to handle product's quantity in Order Model."""
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Order {self.order.id} - Product {self.product.title} - Quantity {self.quantity}"
