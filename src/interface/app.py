from fastapi import FastAPI

from src.config import app_config
from .api import auth_router, cart_router, category_router, product_router, order_router

app = FastAPI(
    title='Меха и шубы',
    description='API интернет-магазина “Меха и шубы“',
    version='1.0',
    contact={
        'name': 'Белых Егор',
        'url': 'https://t.me/popipopich',
        'email': 'eg.belykh@yandex.ru'
    },
    debug=app_config.debug
)

API_V1_PREFIX = '/api/v1'

app.include_router(category_router, prefix=API_V1_PREFIX)
app.include_router(product_router, prefix=API_V1_PREFIX)
app.include_router(auth_router, prefix=API_V1_PREFIX)
app.include_router(cart_router, prefix=API_V1_PREFIX)
app.include_router(order_router, prefix=API_V1_PREFIX)
