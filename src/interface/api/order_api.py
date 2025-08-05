from fastapi import APIRouter, Depends

from src.application.usecase import CreateOrderUseCase
from src.interface.dependency import get_create_order_use_case
from src.interface.security import get_authentication_principal

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
        port: CreateOrderUseCase = Depends(get_create_order_use_case),
        user_id: int = Depends(get_authentication_principal)
) -> None:
    await port.execute(user_id)
