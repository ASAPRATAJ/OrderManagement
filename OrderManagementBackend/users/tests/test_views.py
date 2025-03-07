from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

User = get_user_model()


class UserProfileViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test@example.com",
            company_name="Test Company",
            password="Testpass123!"
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrieve_user_profile(self):
        """Test retrieving the profile of the authenticated user."""
        response = self.client.get("/api/users/profile/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], self.user.email)
        self.assertEqual(response.data["company_name"], self.user.company_name)

    def test_update_user_profile(self):
        """Test updating the profile of the authenticated user."""
        updated_data = {
            "company_name": "Updated Company",
            "phone_number": "+48123456789"
        }
        response = self.client.patch("/api/users/profile/", updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.company_name, "Updated Company")
        self.assertEqual(self.user.phone_number, "+48123456789")


class CustomTokenObtainPairViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test@example.com",
            company_name="Test Company",
            password="Testpass123!"
        )

    def test_obtain_token_with_valid_credentials(self):
        """Test obtaining JWT tokens with valid credentials."""
        data = {
            "email": "test@example.com",
            "password": "Testpass123!"
        }
        response = self.client.post("/api/users/login/", data, format="json")  # Użyj rzeczywistej ścieżki URL
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_obtain_token_with_invalid_credentials(self):
        """Test obtaining JWT tokens with invalid credentials."""
        data = {
            "email": "test@example.com",
            "password": "wrongpassword"
        }
        response = self.client.post("/api/users/login/", data, format="json")  # Użyj rzeczywistej ścieżki URL
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class UserCreateViewTestCase(APITestCase):
    def test_create_user_with_valid_data(self):
        """Test creating a new user with valid data."""
        data = {
            "email": "newuser@example.com",
            "company_name": "New User",
            "password": "Newpass123!"
        }
        response = self.client.post("/api/users/register/", data, format="json")  # Użyj rzeczywistej ścieżki URL
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, "newuser@example.com")

    def test_create_user_with_invalid_data(self):
        """Test creating a new user with invalid data."""
        data = {
            "email": "invalidemail",  # Nieprawidłowy email
            "company_name": "New User",
            "password": "short"  # Nieprawidłowe hasło
        }
        response = self.client.post("/api/users/register/", data, format="json")  # Użyj rzeczywistej ścieżki URL
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)


class UserListViewTestCase(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_user(
            email="admin@example.com",
            company_name="Admin Company",
            password="Adminpass123!",
            is_staff=True,
            is_superuser=True
        )
        self.regular_user = User.objects.create_user(
            email="user@example.com",
            company_name="Regular User",
            password="Userpass123!"
        )

    def test_list_users_as_admin(self):
        """Test listing all users as an admin."""
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get("/api/users/")  # Użyj rzeczywistej ścieżki URL
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Admin i regularny użytkownik

    def test_list_users_as_regular_user(self):
        """Test listing all users as a regular user."""
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.get("/api/users/")  # Użyj rzeczywistej ścieżki URL
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
