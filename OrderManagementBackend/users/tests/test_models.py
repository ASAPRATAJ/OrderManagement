from django.test import TestCase
from users.models import CustomUser
from users.models import CustomUserManager


#Test cases:
# Sprawdzic czy model poprawnie zapisuje sie w bazie (OK)
# Sprawdzic czy model poprawnie jest tworzony (OK)
# sprawdzic czy superuser jest poprawnie tworzony - sprawdzic czy posiada is_staff = True oraz is_superuser = True (OK)
# sprawdzic czy pole defaultowe automatycznie sie dodaja (OK)
# sprawdzic czy haslo jest zhashowane (OK)
# sprawdzic czy nie da sie stworzyc dwoch takich samych uzytkownikow
# sprawdzic czy tworzenie uzytkownika za pomoca emaila jest poprawne
# sprawdzic czy jest normalizacja email lub czy dziala poprawnie
# sprawdzic czy hasło zawiera male litery
# sprawdzic czy haslo zawiera duze litery
# sprawdzic czy haslo zawiera minimum 8 znakow
# sprawdzic czy haslo zawiera przynajmniej jeden znak specjalny
#

class CustomUserTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email='user@example.com',
            company_name='Example User',
            password='Testpass123!'
        )
        self.superuser = CustomUser.objects.create_superuser(
            email='superuser@example.com',
            company_name='Super User',
            password='Testpass123!'
        )

    def test_model_is_saved_in_db(self):
        user_quantity = CustomUser.objects.count()
        self.assertEqual(user_quantity, 2)

    def test_model_user_creation(self):
        self.assertEqual(self.user.email, 'user@example.com')
        self.assertEqual(self.user.company_name, 'Example User')
        self.assertTrue(self.user.check_password, 'Testpass123!')

    def test_model_superuser_creation(self):
        self.assertEqual(self.superuser.email, 'superuser@example.com')
        self.assertEqual(self.superuser.company_name, 'Super User')
        self.assertTrue(self.superuser.check_password, 'Testpass123!')
        self.assertTrue(self.superuser.is_staff)
        self.assertTrue(self.superuser.is_superuser)

    def test_model_default_fields_are_added(self):
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertIsNotNone(self.user.date_joined)

    def test_model_password_is_hashed(self):
        self.assertNotEqual(self.user.password, 'testpass123')
        self.assertTrue(self.user.check_password, 'Testpass123!')

    def test_creating_two_same_users_raises_error(self):
        with self.assertRaises(Exception):
            CustomUser.objects.create_user(
                email='user@example.com',
                company_name='Example User2',
                password='Testpass123!'
            )

    def test_email_normalization(self):
        email = 'EMAIL@EXAMPLE.COM'
        user1 = CustomUser.objects.create_user(
            email=email,
            company_name='Example User1',
            password='Testpass123!'
        )
        self.assertEqual(user1.email, 'email@example.com')

    def test_user_must_have_email(self):
        with self.assertRaises(ValueError) as context:
            CustomUser.objects.create_user(
                email='',
                company_name='Example User',
                password='Testpass123!',
            )
        self.assertEqual(str(context.exception), 'The Email field must be set')


    def test_superuser_must_have_is_superuser_true(self):
        with self.assertRaises(ValueError):
            CustomUser.objects.create_superuser(
                email='superuser@example.com',
                company_name='Super User',
                password='Testpass123!',
                is_superuser=False,
            )

    def test_superuser_must_have_is_staff_true(self):
        with self.assertRaises(ValueError):
            CustomUser.objects.create_superuser(
                email='superuser@example.com',
                company_name='Super User',
                password='Testpass123!',
                is_staff=False
            )

    def test_user_str_method(self):
        self.assertEqual(str(self.user), 'Example User')

    def test_password_with_less_than_8_characters_gives_an_error(self):
        with self.assertRaises(ValueError) as context:
            CustomUser.objects.create_user(
                email='user@example.com',
                company_name='Example User',
                password='testpas'
            )
        self.assertEqual(str(context.exception), 'Password must contain at least 8 characters')

    def test_password_with_no_uppercase_gives_an_error(self):
        with self.assertRaises(ValueError) as context:
            CustomUser.objects.create_user(
                email='user@example.com',
                company_name='Example User',
                password='password1!'
            )
        self.assertEqual(str(context.exception), 'Password must contain at least one uppercase letter')

    def test_password_with_no_lowercase_gives_an_error(self):
        with self.assertRaises(ValueError) as context:
            CustomUser.objects.create_user(
                email='user@example.com',
                company_name='Example User',
                password='PASSWORD1!'
            )
        self.assertEqual(str(context.exception), 'Password must contain at least one lowercase letter')

    def test_password_with_no_digit_gives_an_error(self):
        with self.assertRaises(ValueError) as context:
            CustomUser.objects.create_user(
                email='user@example.com',
                company_name='Example User',
                password='Password!'
            )
        self.assertEqual(str(context.exception), 'Password must contain at least one digit')

    def test_password_with_no_special_character_gives_an_error(self):
        with self.assertRaises(ValueError) as context:
            CustomUser.objects.create_user(
                email='user@example.com',
                company_name='Example User',
                password='Password1'
            )
        self.assertEqual(str(context.exception), 'Password must contain at least one special character')
