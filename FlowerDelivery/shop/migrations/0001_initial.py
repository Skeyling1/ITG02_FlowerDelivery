# Generated by Django 5.1.5 on 2025-02-23 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good_title', models.CharField(max_length=50, verbose_name='Название товара')),
                ('price', models.CharField(max_length=50, verbose_name='Цена')),
                ('picture', models.CharField(max_length=50, verbose_name='Изображение')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50, verbose_name='Пользователь')),
                ('goods', models.CharField(max_length=50, verbose_name='Товары')),
                ('picture', models.CharField(max_length=50, verbose_name='Изображение')),
            ],
        ),
    ]
