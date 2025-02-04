# ITG02
Сайт с доставкой цветов и получение заказов через Telegram бота



Цель проекта:
Создание простого веб-сайта для заказа доставки цветов с базовой интеграцией заказов через Telegram бота.

Общая информация о проекте:
Проект включает разработку простого веб-сайта для заказа цветов и простого Telegram бота для приема заказов.



Область применения
Описание проблемы:
Необходимость упрощенного способа заказа цветов через интернет и мессенджер.



Пользователи системы:
Частные лица, заказывающие цветы.



Основные ограничения и допущения:
Пользователи должны иметь доступ к интернету и Telegram. Заказы принимаются только в рабочее время.



Функциональные требования
- Веб-сайт:
    - Регистрация пользователей.
    - Просмотр каталога цветов.
    - Оформление заказа.
- Telegram бот:
    - Получение заказов с информацией о букетах и доставке.



Общая архитектура системы:
- Веб-приложение на Django.
- Серверная часть на Python с использованием Django.
- Описание подсистем и модулей:
- Модуль регистрации.
- Модуль каталога товаров.
- Модуль оформления заказа.



Модель данных
- Таблица пользователей (ID, имя, email).
- Таблица товаров (ID, название, цена).
- Таблица заказов (ID, пользователь, товары).



Методы и стратегии тестирования:
- Юнит-тестирование.
 
