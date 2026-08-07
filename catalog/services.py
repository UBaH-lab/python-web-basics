from django.core.cache import cache
from catalog.models import Product, Category


def get_products_by_category(category_id):
    """Возвращает список продуктов в указанной категории с кешированием"""
    cache_key = f'category_{category_id}'
    products = cache.get(cache_key)
    if products is None:
        products = list(Product.objects.filter(category_id=category_id))
        cache.set(cache_key, products, 300)  # TTL 5 минут
    return products
