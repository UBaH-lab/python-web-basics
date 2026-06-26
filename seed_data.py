import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from catalog.models import Category, Product

# Удаляем все данные
Product.objects.all().delete()
Category.objects.all().delete()

# Создаём категории
cat1 = Category.objects.create(
    name='Смартфоны',
    description='Мобильные телефоны'
)
cat2 = Category.objects.create(
    name='Ноутбуки',
    description='Портативные компьютеры'
)
cat3 = Category.objects.create(
    name='Планшеты',
    description='Планшетные компьютеры'
)

# Создаём продукты
Product.objects.create(
    name='iPhone 15',
    description='Флагман Apple',
    price=999.99,
    category=cat1
)
Product.objects.create(
    name='Samsung Galaxy S24',
    description='Флагман Samsung',
    price=899.99,
    category=cat1
)
Product.objects.create(
    name='MacBook Pro 14',
    description='Профессиональный ноутбук',
    price=1999.99,
    category=cat2
)
Product.objects.create(
    name='iPad Pro',
    description='Планшет Apple',
    price=1099.99,
    category=cat3
)

print('Данные созданы!')

# Создаём фикстуры через Django management command
from django.core.management import call_command
import json

# Создаём папку если её нет
os.makedirs('catalog/fixtures', exist_ok=True)

# Получаем данные и сохраняем с правильной кодировкой
categories = []
for cat in Category.objects.all():
    categories.append({
        "model": "catalog.category",
        "pk": cat.pk,
        "fields": {
            "name": cat.name,
            "description": cat.description
        }
    })

products = []
for prod in Product.objects.all():
    products.append({
        "model": "catalog.product",
        "pk": prod.pk,
        "fields": {
            "name": prod.name,
            "description": prod.description,
            "image": "",
            "category": prod.category.pk,
            "price": str(prod.price),
            "created_at": prod.created_at.isoformat(),
            "updated_at": prod.updated_at.isoformat()
        }
    })

with open('catalog/fixtures/categories.json', 'w', encoding='utf-8') as f:
    json.dump(categories, f, ensure_ascii=False, indent=2)

with open('catalog/fixtures/products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent=2)

print('Фикстуры созданы!')