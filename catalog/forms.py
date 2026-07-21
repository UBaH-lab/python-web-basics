from django import forms
from catalog.models import Product, Category


# Задание 1: Список запрещённых слов вынесен в константу
FORBIDDEN_WORDS = [
    'казино',
    'криптовалюта',
    'крипта',
    'биржа',
    'дешево',
    'бесплатно',
    'обман',
    'полиция',
    'радар',
]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category']

    # Задание 3: Стилизация формы через __init__
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.ClearableFileInput):
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-control'

        self.fields['name'].widget.attrs['placeholder'] = 'Введите название продукта'
        self.fields['description'].widget.attrs['placeholder'] = 'Введите описание продукта'
        self.fields['price'].widget.attrs['placeholder'] = 'Введите цену'

    # Задание 1: Валидация названия
    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        name_lower = name.lower()
        for word in FORBIDDEN_WORDS:
            if word in name_lower:
                raise forms.ValidationError(
                    f'Слово "{word}" запрещено для использования в названии продукта.'
                )
        return name

    # Задание 1: Валидация описания
    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        if description:
            description_lower = description.lower()
            for word in FORBIDDEN_WORDS:
                if word in description_lower:
                    raise forms.ValidationError(
                        f'Слово "{word}" запрещено для использования в описании продукта.'
                    )
        return description

    # Задание 2: Валидация цены
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError(
                'Цена не может быть отрицательной. Пожалуйста, введите положительное значение.'
            )
        return price

    # Доп. задание: Валидация изображения
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            max_size = 5 * 1024 * 1024  # 5 МБ
            if image.size > max_size:
                raise forms.ValidationError(
                    'Размер изображения не должен превышать 5 МБ.'
                )
            import os
            ext = os.path.splitext(image.name)[1].lower()
            if ext not in ['.jpg', '.jpeg', '.png']:
                raise forms.ValidationError(
                    'Допустимые форматы изображения: JPEG, PNG.'
                )
        return image
