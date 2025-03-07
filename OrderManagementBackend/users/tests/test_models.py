from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserModelTest(TestCase):
    def setUp(self):
        # Tworzymy użytkownika przed każdym testem
        self.user = User.objects.create_user(
            email="test@example.com",
            company_name="Test Company",
            password="Testpass123#"
        )

    def test_create_user(self):
        """Test creating a regular user."""
        user = User.objects.create_user(
            email="test2@example.com",
            company_name="Test Company 2",
            password="Testpass123#"
        )
        self.assertEqual(user.email, "test2@example.com")
        self.assertEqual(user.company_name, "Test Company 2")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """Test creating a superuser."""
        superuser = User.objects.create_superuser(
            email="admin@example.com",
            company_name="Admin Company",
            password="Testpass123#"
        )
        self.assertEqual(superuser.email, "admin@example.com")
        self.assertEqual(superuser.company_name, "Admin Company")
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_email_normalization(self):
        """Test email normalization."""
        email = "Test3@Example.COM"
        user = User.objects.create_user(
            email=email,
            company_name="Test Company",
            password="Testpass123#"
        )
        self.assertEqual(user.email, email.lower())

    def test_unique_email(self):
        """Test that email must be unique."""
        # Próbujemy utworzyć drugiego użytkownika z tym samym e-mailem
        user = User(
            email="test@example.com",
            company_name="Another Company",
            password="Testpass123#"
        )

        # Sprawdzamy, czy walidacja zgłasza błąd (e-mail musi być unikalny)
        with self.assertRaises(ValidationError):
            user.full_clean()

    def test_password_validation(self):
        bad_password = "testpass123"
        bad_password2 = "test"
        bad_password3 = "testpass123#"
        bad_password4 = "Testpass123"
        correct_password = "Testpass123#"

        self.user.set_password(correct_password)

        with self.assertRaises(ValidationError):
            self.user.set_password(bad_password)
            self.user.set_password(bad_password2)
            self.user.set_password(bad_password3)
            self.user.set_password(bad_password4)

    def test_nip_validation(self):
        """Test NIP validation."""
        # Update user from setUp with valid NIP
        self.user.nip = "1234567890"  # Valid NIP
        self.user.full_clean()  # it should pass without errors

        # Update user with invalid NIP
        self.user.nip = "12345"  # Invalid NIP
        with self.assertRaises(ValidationError):
            self.user.full_clean()  # It should raise error

    def test_phone_number_validation(self):
        """Test Phone Number validation."""
        # Update user from setUp with valid Phone number
        phone_number = "+48796207454"
        phone_number2 = "796207454"
        bad_phone_number = "12312323"

        self.user.phone_number = phone_number
        self.user.full_clean()

        self.user.phone_number = phone_number2
        self.user.full_clean()

        self.user.phone_number = bad_phone_number
        with self.assertRaises(ValidationError):
            self.user.full_clean()

    def test_default_values(self):
        """Test default values for is_active and date_joined."""
        user = self.user

        self.assertTrue(user.is_active)
        self.assertIsNotNone(user.date_joined)

