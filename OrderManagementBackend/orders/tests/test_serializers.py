from django.test import TestCase
from django.utils.dateparse import parse_datetime

from orders.serializers import OrderProductSerializer, OrderCreateSerializer, OrderListSerializer
from products.models import Product
from orders.models import OrderProduct, Order
from users.models import CustomUser

from rest_framework.test import APIRequestFactory


class OrderCreateSerializerTestCase(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email='user@example.com',
            company_name='Example Company',
            password='Testpass123!',
        )
        self.product1 = Product.objects.create(title="Product 1", price=100)
        self.product2 = Product.objects.create(title="Product 2", price=200)

        self.factory = APIRequestFactory()

    def test_create_order(self):
        """Test tworzenia zamówienia za pomocą OrderCreateSerializer"""
        data = {
            'products': [
                {'product_id': self.product1.id, 'quantity': 2},
                {'product_id': self.product2.id, 'quantity': 1}
            ]
        }

        # Tworzymy fałszywe żądanie
        request = self.factory.post('/fake-url')
        request.user = self.user

        # Przekazujemy request w kontekście serializera
        serializer = OrderCreateSerializer(data=data, context={'request': request})
        self.assertTrue(serializer.is_valid())
        order = serializer.save()

        # Sprawdzamy, czy zamówienie zostało poprawnie stworzone
        self.assertEqual(order.user, self.user)
        self.assertEqual(order.products.count(), 2)


class OrderProductSerializerTestCase(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email='user@example.com',
            company_name='Example Company',
            password='Testpass123!',
        )
        self.product = Product.objects.create(title="Product 1", price=100)
        self.order = Order.objects.create(user=self.user)
        self.order_product = OrderProduct.objects.create(order=self.order, product=self.product, quantity=2)

    def test_order_product_serializer_data(self):
        """Test poprawności danych zwracanych przez OrderProductSerializer"""
        serializer = OrderProductSerializer(self.order_product)
        expected_data = {
            'product_id': self.product.id,
            'quantity': 2
        }
        self.assertEqual(serializer.data, expected_data)


class OrderListSerializerTestCase(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email='user@example.com',
            company_name='Example Company',
            password='Testpass123!',
        )
        self.product1 = Product.objects.create(title="Product 1", price=100)
        self.product2 = Product.objects.create(title="Product 2", price=200)
        self.order = Order.objects.create(user=self.user)
        OrderProduct.objects.create(order=self.order, product=self.product1, quantity=2)
        OrderProduct.objects.create(order=self.order, product=self.product2, quantity=1)

    def test_order_list_serializer_data(self):
        """Test poprawności danych zwracanych przez OrderListSerializer"""
        serializer = OrderListSerializer(self.order)
        expected_data = {
            'id': self.order.id,
            'created_at': self.order.created_at.isoformat(),
            'user': self.user.id,
            'products': [
                {'product_id': self.product1.id, 'product_title': self.product1.title, 'quantity': 2},
                {'product_id': self.product2.id, 'product_title': self.product2.title, 'quantity': 1},
            ]
        }
        # Porównanie pól id, user oraz produktów
        self.assertEqual(serializer.data['id'], expected_data['id'])
        self.assertEqual(serializer.data['user'], expected_data['user'])
        self.assertEqual(serializer.data['products'], expected_data['products'])

        # Porównanie daty z ignorowaniem strefy czasowej
        self.assertEqual(parse_datetime(serializer.data['created_at']), parse_datetime(expected_data['created_at']))
