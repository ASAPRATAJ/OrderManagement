from django.db import models
from users.models import CustomUser
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order ID{self.id}, created by {self.user}"
