# Django Catalog

Учебный проект каталога товаров на Django.

## Модели

- **Category** — категории товаров
- **Product** — товары

## Запуск проекта

pip install -r requirements.txt
python manage.py migrate
python manage.py seed_products
python manage.py runserver

## Страницы

- `/` — Главная со списком товаров
- `/products/<id>/` — Страница товара
- `/products/create/` — Добавление товара
- `/contacts/` — Контакты

## Шаблоны

Структура:

templates/
├── base.html              # Базовый шаблон
├── navbar.html            # Меню
└── catalog/
    ├── home.html          # Список товаров
    ├── product_detail.html # Страница товара
    ├── product_form.html   # Форма добавления
    └── contacts.html       # Контакты

Функционал:

- base.html — Bootstrap 5, блоки title и content
- navbar.html — навигация
- home.html — карточки товаров, truncatechars:100, пагинация
- product_detail.html — детали товара, хлебные крошки
- product_form.html — форма создания товара

## Бонус

- Форма добавления товара (ProductForm)
- Пагинация по 6 товаров

## Тестовые данные

python manage.py seed_products

Создаёт 100 товаров.
