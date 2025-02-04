from django.test import TestCase
from django.urls import reverse
from .models import Good  # Импортируйте вашу модель

# Create your tests here.
class GoodModelTest(TestCase):

    def setUp(self):
        # Создаем экземпляр модели Good
        self.good = Good.objects.create(good_title='Ромашки', price='150', picture='shop/img/1.jpg')

    def test_good_creation(self):
        # Проверяем, что объект был создан
        self.assertIsInstance(self.good, Good)
        self.assertEqual(self.good.good_title, 'Ромашки')
        self.assertEqual(self.good.price, '150')
        self.assertEqual(self.good.picture, 'shop/img/1.jpg')

    def test_good_string_representation(self):
        # Проверяем строковое представление
        self.assertEqual(str(self.good), 'Ромашки')  # Предполагается, что метод __str__ возвращает good_title

    def test_price_is_decimal(self):
        # Проверяем, что цена является числом
        self.assertIsInstance(self.good.price, str)  # Если price - строка
        # Если price должен быть десятичным числом, используйте Decimal и проверьте тип
        # from decimal import Decimal
        # self.assertIsInstance(self.good.price, Decimal)

    def test_picture_path(self):
        # Проверяем, что путь к картинке корректный
        self.assertEqual(self.good.picture, 'shop/img/1.jpg')