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
│   ├── interface/                      # Слой интерфейсов
│   │   ├── api/                                # FastAPI роутеры
│   │   │   └── dto/                                # DTO для API
│   │   ├── dependency/                     # Зависимости FastAPI
│   │   │   └── security/                   # Безопасность
│   │   ├── app.py                          # Конфигурация FastAPI приложения
│   │   └── error_handlers.py               # Обработчики ошибок
│   ├── application/                    # Слой приложения
│   │   ├── usecase/                        # Сценарии использования
│   │   ├── model/                          # Доменные модели
│   │   ├── dto/                            # DTO для приложения
│   │   ├── repository/                     # Интерфейсы репозиториев
│   │   ├── error/                          # Ошибки приложения
│   │   ├── shared/                         # Общие компоненты
│   │   └── utils/                          # Утилиты
│   ├── infrastructure/                 # Слой инфраструктуры
│   │   ├── database/                       # Работа с базой данных
│   │   │   ├── entity/                         # Сущности БД
│   │   │   ├── repository/                     # Реализации репозиториев
│   │   │   ├── migrations/                     # Миграции Alembic
│   │   │   └── database_session.py             # Сессия БД
│   │   ├── object_storage/                 # Файловое хранилище
│   │   │   ├── minio_client.py                     # MinIO клиент
│   │   │   └── minio_product_image_repository.py   # Репозиторий изображений
│   │   └── smtp/                           # Отправка email сообщений
│   │       ├── smtp_client.py                  # SMTP клиент
│   │       └── email_sender.py                 # Отправка писем
│   ├── config/                         # Конфигурация приложения
│   └── main.py                         # Точка входа приложения
├── tests/                      # Тесты
├── docker-compose.local.yaml   # Docker Compose для локальной разработки
├── Dockerfile                  # Docker образ приложения
├── requirements.txt            # Зависимости
└── alembic.ini                 # Конфигурация Alembic
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