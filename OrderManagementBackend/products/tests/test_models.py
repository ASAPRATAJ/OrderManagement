# from django.test import TestCase
# from products.models import Product
#
# # Test Cases:
# # po stworzeniu model sie zapisuje w bazie danych (OK)
# # Czy dane wyjsciowe sa takie same jak wejściowe (OK)
# # Czy po utworzeniu produktu dodaje się automatycznie ustawione zdjęcie (OK)
# # Czy __str__ zwraca title (OK)
#
#
# class ProductTestCase(TestCase):
#     def setUp(self):
#         self.model = Product.objects.create(
#             title='Example',
#             description='Example description',
#             price=40
#         )
#
#     def test_model_is_saved_in_db(self):
#         self.assertIsNotNone(self.model.id)
#
#     def test_model_str_method(self):
#         self.assertEqual(str(self.model), 'Example')
#
#     def test_model_fields_are_correct(self):
#         self.assertEqual(self.model.title, 'Example')
#         self.assertEqual(self.model.description, 'Example description')
#         self.assertEqual(self.model.price, 40)
#
#     def test_model_default_image_is_added(self):
#         self.assertEqual(self.model.image, 'products/images/PolishLodyLogo.jpg')
