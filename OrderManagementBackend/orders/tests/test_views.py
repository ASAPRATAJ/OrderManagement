# from rest_framework import status
# from rest_framework.test import APITestCase, APIClient
# from django.urls import reverse
# from rest_framework_simplejwt.tokens import RefreshToken
# from orders.models import Order, OrderProduct
# from products.models import Product
# from users.models import CustomUser
#
#
# class OrderViewsTestCase(APITestCase):
#
#     def setUp(self):
#         self.client = APIClient()
#
#         # Tworzymy użytkowników
#         self.user = CustomUser.objects.create_user(
#             email='user@example.com',
#             company_name='Example Company',
#             password='Testpass123!'
#         )
#         self.other_user = CustomUser.objects.create_user(
#             email='otheruser@example.com',
#             company_name='Other Company',
#             password='Testpass123!'
#         )
#
#         # Tworzymy produkty
#         self.product1 = Product.objects.create(title="Product 1", price=100)
#         self.product2 = Product.objects.create(title="Product 2", price=200)
#
#         # Token JWT dla użytkownika
#         self.token = str(RefreshToken.for_user(self.user).access_token)
#
#     def authenticate_user(self):
#         """Pomocnicza funkcja do autoryzacji użytkownika"""
#         self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
#
#     def test_create_order(self):
#         """Test poprawnego tworzenia zamówienia"""
#         self.authenticate_user()
#         url = reverse('order-create')
#         data = {
#             "products": [
#                 {"product_id": self.product1.id, "quantity": 2},
#                 {"product_id": self.product2.id, "quantity": 1}
#             ]
#         }
#
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Order.objects.count(), 1)
#         self.assertEqual(OrderProduct.objects.count(), 2)
#
#     def test_create_order_unauthenticated(self):
#         """Test próby utworzenia zamówienia przez niezalogowanego użytkownika"""
#         url = reverse('order-create')
#         data = {
#             "products": [
#                 {"product_id": self.product1.id, "quantity": 2}
#             ]
#         }
#
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
#
#     def test_create_order_with_empty_product_list(self):
#         """Test próby utworzenia zamówienia z pustą listą produktów"""
#         self.authenticate_user()
#         url = reverse('order-create')
#         data = {
#             "products": []  # Pusta lista produktów
#         }
#
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertEqual(response.data['non_field_errors'][0], "To create order, the list cannot be empty.")
