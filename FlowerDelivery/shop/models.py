# Модель данных
# - Таблица пользователей (ID, имя, email).
# - Таблица товаров (ID, название, цена).
# - Таблица заказов (ID, пользователь, товары).

from django.db import models


class Good(models.Model):
	good_title = models.CharField('Название товара', max_length=50)
	price = models.CharField('Цена', max_length=50)
	picture = models.CharField('Изображение', max_length=50)

	def __str__(self):
		return self.good_title


class Order(models.Model):
	user = models.CharField('Пользователь', max_length=50)
	goods = models.CharField('Товары', max_length=50)
	picture = models.CharField('Изображение', max_length=50)

	def __str__(self):
		return self.user