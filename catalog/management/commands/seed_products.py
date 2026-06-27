from django.core.management.base import BaseCommand
from catalog.models import Category, Product
import random


class Command(BaseCommand):
    help = 'Создаёт тестовые продукты'

    def handle(self, *args, **options):
        # Удаляем все продукты перед созданием новых
        Product.objects.all().delete()
        self.stdout.write('Удалены старые продукты')

        # Получаем все категории
        categories = Category.objects.all()

        if not categories.exists():
            self.stdout.write(self.style.ERROR('Нет категорий! Сначала создайте категории.'))
            return

        # Список названий продуктов
        product_names = [
            'Смартфон', 'Планшет', 'Ноутбук', 'Монитор', 'Клавиатура',
            'Мышь', 'Наушники', 'Колонка', 'Камера', 'Принтер',
            'Сканер', 'Роутер', 'Модем', 'Флешка', 'Жесткий диск',
            'SSD', 'Видеокарта', 'Процессор', 'Оперативная память', 'Материнская плата',
            'Блок питания', 'Корпус', 'Кулер', 'Термопаста', 'Кабель',
            'Переходник', 'Зарядка', 'Аккумулятор', 'Чехол', 'Защитное стекло'
        ]

        products_created = 0

        for i in range(100):
            name = f'{random.choice(product_names)} #{i + 1}'
            category = random.choice(categories)
            price = round(random.uniform(100, 10000), 2)

            Product.objects.create(
                name=name,
                description=f'Описание для {name}',
                price=price,
                category=category
            )
            products_created += 1

        self.stdout.write(self.style.SUCCESS(f'Создано {products_created} продуктов!'))