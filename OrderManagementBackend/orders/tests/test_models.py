from django.test import TestCase
from orders.models import Order, OrderProduct
from users.models import CustomUser
from products.models import Product


class OrderModelTestCase(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email='user@example.com',
            company_name='Example Company',
            password='Testpass123!',
        )
        self.product1 = Product.objects.create(title="Product 1", price=100)
        self.product2 = Product.objects.create(title="Product 2", price=200)
        self.order = Order.objects.create(user=self.user)
        self.order_product = OrderProduct.objects.create(order=self.order, product=self.product1, quantity=2)

    def test_order_str(self):
        """Testowanie metody __str__ w modelu Order."""
        expected_str = f"Order ID{self.order.id}, created by {self.user}"
        self.assertEqual(str(self.order), expected_str)

    def test_order_product_str(self):
        """Testowanie metody __str__ w modelu OrderProduct."""
        expected_str = f"Order {self.order.id} - Product {self.product1.title} - Quantity {self.order_product.quantity}"
        self.assertEqual(str(self.order_product), expected_str)
