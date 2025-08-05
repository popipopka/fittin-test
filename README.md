# Бэкенд интернет-магазина "Меха и шубы"

## 📞 Контакты

- **Разработчик**: Белых Егор
- **Telegram**: https://t.me/popipopich
- **Email**: eg.belykh@yandex.ru

## 🛠 Основной стек

- **Python 3.13.1**
- **FastAPI**
- **Pydantic**
- **SQLAlchemy**
- **PostgreSQL 17**
- **Alembic**
- **MinIO**
- **MailHog**
- **Docker**
- **PyUnit**

## 📁 Структура проекта

Проект использует архитектуру Clean Architecture с разделением на слои:

- **interface** - внешние интерфейсы (API, обработка ошибок, безопасность)
- **application** - бизнес-логика и use cases
- **infrastructure** - внешние сервисы (база данных, файловое хранилище, SMTP)

```
fittin-test/
├── src/                            # Исходный код приложения
│   ├── interface/                   # Слой интерфейсов
│   │   ├── api/                      # FastAPI роутеры
│   │   │   ├── auth_api.py              # Аутентификация
│   │   │   ├── cart_api.py              # Корзина
│   │   │   ├── category_api.py          # Категории
│   │   │   ├── order_api.py             # Заказы
│   │   │   ├── product_api.py           # Товары
│   │   │   └── dto/                     # DTO для API
│   │   ├── dependency/                  # Зависимости FastAPI
│   │   ├── security/                    # Безопасность и JWT
│   │   ├── app.py                       # Конфигурация FastAPI приложения
│   │   └── error_handlers.py            # Обработчики ошибок
│   ├── application/                  # Слой приложения
│   │   ├── usecase/                     # Бизнес-логика и use cases
│   │   │   ├── mapper/                     # Маппинг между слоями
│   │   │   ├── get_product_use_case.py     # Получение товара
│   │   │   ├── get_products_use_case.py    # Получение списка товаров
│   │   │   ├── get_categories_use_case.py  # Получение категорий
│   │   │   ├── login_use_case.py           # Вход в систему
│   │   │   ├── register_use_case.py        # Регистрация
│   │   │   ├── issue_access_token_use_case.py # Выдача токенов
│   │   │   ├── add_item_to_cart_use_case.py   # Добавление в корзину
│   │   │   ├── get_items_from_cart_use_case.py # Получение корзины
│   │   │   ├── update_item_in_cart_use_case.py # Обновление корзины
│   │   │   ├── remove_item_from_cart_use_case.py # Удаление из корзины
│   │   │   └── create_order_use_case.py        # Создание заказа
│   │   ├── model/                       # Доменные модели
│   │   ├── dto/                         # DTO для приложения
│   │   ├── repository/                  # Интерфейсы репозиториев
│   │   ├── error/                       # Ошибки приложения
│   │   ├── shared/                      # Общие компоненты
│   │   └── utils/                       # Утилиты
│   ├── infrastructure/               # Слой инфраструктуры
│   │   ├── database/                    # Работа с базой данных
│   │   │   ├── entity/                     # Сущности БД
│   │   │   ├── repository/                 # Реализации репозиториев
│   │   │   ├── migrations/                 # Миграции Alembic
│   │   │   └── database_session.py         # Сессии БД
│   │   ├── object_storage/                # Файловое хранилище
│   │   │   ├── minio_client.py                # Клиент MinIO
│   │   │   └── minio_product_image_repository.py # Репозиторий изображений
│   │   └── smtp/                         # Отправка email
│   │       ├── smtp_client.py                # SMTP клиент
│   │       └── email_sender.py               # Отправка писем
│   ├── config/                       # Конфигурация приложения
│   └── main.py                       # Точка входа приложения
├── tests/                            # Тесты
├── docker-compose.local.yaml         # Docker Compose для локальной разработки
├── Dockerfile                        # Docker образ приложения
├── requirements.txt                  # Python зависимости
└── alembic.ini                       # Конфигурация Alembic
```

## 🔧 Основные эндпоинты

- `/api/v1/categories` - категории товаров
- `/api/v1/product`, `/api/v1/products` - товары
- `/api/v1/auth` - аутентификация
- `/api/v1/cart` - корзина
- `/api/v1/orders` - заказы

## 🚀 Запуск приложения

1. Запустить PostgreSQL, Minio, MailHog, используя Docker Compose

```bash
  docker-compose -f docker-compose.local.yaml up -d postgres minio mailhog 
```

2. Выполнить миграции БД через alembic:

```bash
  alembic upgrade head
```

### Запуск через Docker Compose

3. Запустить сервис с приложением через Docker Compose

```bash
   docker-compose -f docker-compose.local.yaml up -d app
```

4. Приложение будет доступно по адресу: http://localhost:8001


5. Документация будет доступна по адресам:

- Swagger UI: http://localhost:8001/docs
- ReDoc: http://localhost:8001/redoc

### Без Docker Compose

3. Запустить приложение командой

```bash
  uvicorn src.main:app
```

4. Приложение будет доступно по адресу: http://localhost:8000


5. Документация будет доступна по адресам:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🧪 Тестирование

Для запуска тестов:

```bash
  python -m unittest discover
```