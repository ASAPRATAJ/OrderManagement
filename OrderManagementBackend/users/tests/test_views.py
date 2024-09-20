from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import CustomUser
from orders.models import Order, OrderProduct
from products.models import Product


class UserOrderListViewTestCase(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email='user@example.com',
            company_name='Example Company',
            password='Testpass123!',
        )

        self.other_user = CustomUser.objects.create_user(
            email='otheruser@example.com',
            company_name='Other User Example',
            password='Testpass123!'
        )

        # Tworzymy produkty
        self.product1 = Product.objects.create(title="Example product", price=40)
        self.product2 = Product.objects.create(title="Example product2", price=50)

        # Tworzymy zamówienia
        self.order1 = Order.objects.create(user=self.user)
        self.order2 = Order.objects.create(user=self.other_user)

        # Tworzymy relacje w OrderProduct
        OrderProduct.objects.create(order=self.order1, product=self.product1, quantity=2)
        OrderProduct.objects.create(order=self.order1, product=self.product2, quantity=1)

        OrderProduct.objects.create(order=self.order2, product=self.product1, quantity=3)

        self.client = APIClient()

    def get_token(self):
        """Pomocnicza metoda do uzyskania tokenu JWT."""
        refresh = RefreshToken.for_user(self.user)
        return str(refresh.access_token)

    def test_unauthenticated_user_cannot_see_orders(self):
        # Nie ustawiamy tokenu autoryzacyjnego
        url = reverse('user-orders')
        response = self.client.get(url)

        # Sprawdzamy, czy odpowiedź to 401 Unauthorized
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_see_their_orders(self):
        # Pobieramy token JWT
        token = self.get_token()

        # Ustawiamy nagłówek autoryzacji z tokenem
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        # Pobieramy zamówienia użytkownika
        url = reverse('user-orders')  # Zakładamy, że tak się nazywa URL
        response = self.client.get(url)
        print(response.data[0]['products'][0]['product_title'])

        # Sprawdzamy czy zwrócone zamówienia są tylko tego użytkownika
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Tylko 1 zamówienie dla user@example.com
        self.assertEqual(response.data[0]['products'][0]['product_title'], self.product1.title)
        self.assertEqual(response.data[0]['products'][1]['product_title'], self.product2.title)
        self.assertEqual(response.data[0]['id'], self.order1.id)
