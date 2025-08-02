from fastapi import APIRouter, Depends

from src.adapter.input_port_fast_api.dependency import get_authentication_principal, get_create_order_port
from src.core.port.input import CreateOrderPort

router = APIRouter(
    prefix='/order',
    tags=['Заказы'],
    responses={
        401: {'description': 'Пользователь не аутентифицирован'}
    }
)


@router.get(
    '',
    summary='Создать заказ',
    description='Создает заказ из товаров в корзине и очищает её',
    responses={
        200: {'description': 'Заказ создан', 'content': None},
        404: {'description': 'Корзина пустая'},
    }
)
async def create_order(
        port: CreateOrderPort = Depends(get_create_order_port),
        user_id: int = Depends(get_authentication_principal)
) -> None:
    await port.execute(user_id)
