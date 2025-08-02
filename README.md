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

- **core** - доменная логика и бизнес-правила
- **application** - use cases и координация между слоями
- **adapter** - внешние интерфейсы (API, база данных, файловое хранилище)

```
fittin-test/
├── src/                            # Исходный код приложения
│   ├── adapter/                     # Адаптеры
│   │   ├── input_port_fast_api/       # FastAPI роутеры
│   │   ├── output_port_postgresql/    # PostgreSQL адаптер
│   │   ├── output_port_minio/         # MinIO адаптер
│   │   └── output_port_smtp/          # SMTP адаптер
│   ├── application/                 # Слой приложения
│   │   ├── usecase/                   # Бизнес-логика
│   │   ├── mappers.py                 # Маппинг между слоями
│   │   └── error/                     # Ошибки приложения
│   ├── core/                        # Ядро приложения
│   │   ├── model/                     # Доменные модели
│   │   ├── port/                      # Интерфейсы портов
│   │   ├── error/                     # Доменные ошибки
│   │   └── utils/                     # Утилиты
│   ├── config/                      # Конфигурация приложения
│   └── main.py                      # Точка входа приложения
├── tests/                           # Тесты
├── docker-compose.local.yaml        # Docker Compose для локальной разработки
├── Dockerfile                       # Docker образ приложения
├── requirements.txt                 # Python зависимости
└── alembic.ini                      # Конфигурация Alembic
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