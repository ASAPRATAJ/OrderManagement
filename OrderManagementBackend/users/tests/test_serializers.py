from rest_framework.test import APITestCase
from users.models import CustomUser
from users.serializers import CustomUserSerializer, ListCustomUserSerializer, CustomTokenObtainPairSerializer
from rest_framework.exceptions import ValidationError


class CustomUserSerializerTestCase(APITestCase):

    def setUp(self):
        self.user_data = {
            'email': 'user@example.com',
            'password': 'Testpass123!',
            'company_name': 'Example User',
            'is_staff': False,
            'is_superuser': False
        }

        self.user = CustomUser.objects.create_user(**self.user_data)

    def test_serializer_with_valid_data(self):
        serializer = CustomUserSerializer(instance=self.user)
        expected_data = {
            'id': self.user.id,
            'email': self.user.email,
            'company_name': self.user.company_name,
            'is_staff': self.user.is_staff,
            'is_superuser': self.user.is_superuser
        }
        self.assertEqual(serializer.data, expected_data)

    def test_serializer_create_user(self):
        valid_data = {
            'email': 'newuser@example.com',
            'password': 'Newpass123!',
            'company_name': 'New User'
        }
        serializer = CustomUserSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()

        self.assertEqual(user.email, valid_data['email'])
        self.assertTrue(user.check_password(valid_data['password']))
        self.assertEqual(user.company_name, valid_data['company_name'])

    def test_serializer_raises_validation_error_on_invalid_password(self):
        invalid_data = {
            'email': 'user2@example.com',
            'password': 'short',
            'company_name': 'User2'
        }
        serializer = CustomUserSerializer(data=invalid_data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
            serializer.save()


class ListCustomUserSerializerTestCase(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email='user@example.com',
            company_name='Example User',
            password='Testpass123!',
            is_staff=True,
            is_superuser=False
        )

    def test_list_custom_user_serializer(self):
        serializer = ListCustomUserSerializer(instance=self.user)
        expected_data = {
            'id': self.user.id,
            'company_name': self.user.company_name,
            'is_staff': self.user.is_staff,
            'is_superuser': self.user.is_superuser
        }
        self.assertEqual(serializer.data, expected_data)


class CustomTokenObtainPairSerializerTestCase(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email='user@example.com',
            company_name='Example User',
            password='Testpass123!',
            is_staff=True,
            is_superuser=False
        )

    def test_custom_token_contains_is_staff_and_is_superuser(self):
        serializer = CustomTokenObtainPairSerializer()
        token = serializer.get_token(self.user)

        self.assertIn('is_staff', token)
        self.assertIn('is_superuser', token)
        self.assertEqual(token['is_staff'], self.user.is_staff)
        self.assertEqual(token['is_superuser'], self.user.is_superuser)
