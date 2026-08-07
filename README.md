# Django Catalog — Интернет-магазин

Веб-приложение интернет-магазина на Django с кешированием Redis,
авторизацией пользователей и ролевой моделью доступа.

## 🛠 Технологии
- Python 3.13
- Django 6.0
- PostgreSQL
- Redis (кеширование)
- Bootstrap 5
- SMTP (email-отправка)

## ⚡ Функционал
- 📋 Каталог товаров с пагинацией (по 6 на страницу)
- ✏️ CRUD-операции (создание, редактирование, удаление)
- 🔐 Авторизация и регистрация пользователей
- 👤 Ролевая модель доступа (владелец / модератор)
- 🚀 Кеширование страниц и данных через Redis
- ✅ Валидация форм
- 🖼 Загрузка изображений товаров
- 📧 Email-отправка через SMTP

## 📐 Структура проекта
config/ # Настройки Django (settings, urls, wsgi) catalog/ # Приложение каталога товаров blog/ # Приложение блога users/ # Приложение пользователей templates/ # Шаблоны (base, navbar, страницы) static/ # Статические файлы (CSS, JS, изображения) media/ # Загруженные изображения товаров


## 🚀 Запуск
```bash
git clone https://github.com/UBaH-lab/Django.git
cd Django

# Виртуальное окружение
python -m venv .venv
.venv\Scripts\activate

# Зависимости
pip install -r requirements.txt

# База данных
python manage.py migrate

# Тестовые данные
python manage.py seed_products

# Запуск
python manage.py runserver
📌 Страницы
/ — Каталог товаров (главная)
/product/<id>/ — Страница товара
/product/create/ — Добавление товара
/category/<id>/ — Товары по категории
/contacts/ — Контакты
/blog/ — Блог
