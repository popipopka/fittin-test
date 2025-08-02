from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from src.adapter.input_port_fast_api import auth_router
from src.adapter.input_port_fast_api import cart_router
from src.adapter.input_port_fast_api import category_router
from src.adapter.input_port_fast_api import order_router
from src.adapter.input_port_fast_api import product_router
from src.application.error import AuthenticationError
from src.config import app_config
from src.core.error import RecordNotFoundError, RecordAlreadyExistsError

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


@app.exception_handler(RecordNotFoundError)
def handle_record_not_found_error(req: Request, exc: RecordNotFoundError):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                        content={'detail': str(exc)})


@app.exception_handler(RecordAlreadyExistsError)
def handle_record_already_exists_error(req: Request, exc: RecordAlreadyExistsError):
    return JSONResponse(status_code=status.HTTP_409_CONFLICT,
                        content={'detail': str(exc)})


@app.exception_handler(AuthenticationError)
def handle_authentication_error(req: Request, exc: AuthenticationError):
    return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,
                        content={'detail': str(exc)})


@app.exception_handler(Exception)
async def handle_exception_handler(req: Request, exc: Exception):
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        content={"detail": str(exc) if app_config.debug else 'Внутренняя ошибка сервера'})
