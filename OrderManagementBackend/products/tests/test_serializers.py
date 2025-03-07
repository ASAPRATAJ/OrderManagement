# from rest_framework.test import APITestCase
# from products.serializers import ProductSerializer
# from products.models import Product
#
# # Test Cases:
# # Czy pola  jest prawidlowo serializowany
#
#
# class ProductSerializerTestCase(APITestCase):
#     def setUp(self):
#         self.product = Product.objects.create(
#             title='Example',
#             description='Example description',
#             price=40,
#         )
#
#     def test_serialization(self):
#         serializer = ProductSerializer(self.product)
#
#         expected_data = {
#             'id': self.product.id,
#             'title': 'Example',
#             'description': 'Example description',
#             'price': 40,
#             'image': '/media/products/images/PolishLodyLogo.jpg'
#         }
#
#         self.assertEqual(serializer.data, expected_data)
#
#     def test_deserialization(self):
#         example_data = {
#             'title': 'Example',
#             'description': 'Example description',
#             'price': 40
#         }
#         serializer = ProductSerializer(data=example_data)
#         self.assertTrue(serializer.is_valid())
#         product = serializer.save()
#         self.assertEqual(product.title, 'Example')
#         self.assertEqual(product.description, 'Example description')
#         self.assertEqual(product.price, 40)
#         self.assertEqual(product.image, 'products/images/PolishLodyLogo.jpg')
#
#     def test_invalid_price_validation(self):
#         example_data = {
#             'title': 'Example',
#             'description': 'Example description',
#             'price': 'fourty'
#         }
#         serializer = ProductSerializer(data=example_data)
#         self.assertFalse(serializer.is_valid())
#         self.assertIn('price', serializer.errors)
#
#     def test_missing_title_field(self):
#         example_data = {
#             'description': 'Example description',
#             'price': 40
#         }
#         serializer = ProductSerializer(data=example_data)
#         self.assertFalse(serializer.is_valid())
#         self.assertIn('title', serializer.errors)
#
#     def test_missing_description_field(self):
#         example_data = {
#             'title': 'Example',
#             'price': 40
#         }
#         serializer = ProductSerializer(data=example_data)
#         self.assertFalse(serializer.is_valid())
#         self.assertIn('description', serializer.errors)
#
#     def test_missing_price_field(self):
#         example_data = {
#             'title': 'Example',
#             'description': 'Example description'
#         }
#         serializer = ProductSerializer(data=example_data)
#         self.assertFalse(serializer.is_valid())
#         self.assertIn('price', serializer.errors)
#
#     def test_default_image(self):
#         example_data = {
#             'title': 'Example',
#             'description': 'Example description',
#             'price': 40
#         }
#         serializer = ProductSerializer(data=example_data)
#         self.assertTrue(serializer.is_valid())
#         product = serializer.save()
#         self.assertEqual(product.image.name, 'products/images/PolishLodyLogo.jpg')
#
#     def test_invalid_image_field(self):
#         example_data = {
#             'title': 'Example',
#             'description': 'Example description',
#             'price': 40,
#             'image': 'for example string field instead of image'
#         }
#         serializer = ProductSerializer(data=example_data)
#         self.assertFalse(serializer.is_valid())
#         self.assertIn('image', serializer.errors)
#
#
#
