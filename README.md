# Django project

Учебный проект на Django с приложением `catalog`.

## Запуск проекта

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
# Django Catalog

Проект каталога товаров на Django.

## Модели

- **Category** — категории товаров
- **Product** — товары

## Команда для создания тестовых данных

```bash
python manage.py seed_products
```