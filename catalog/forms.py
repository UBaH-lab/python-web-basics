from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    """
    Форма для создания нового продукта.
    Включает поля name, price и category.
    """
    class Meta:
        model = Product
        fields = ['name', 'price', 'category']
