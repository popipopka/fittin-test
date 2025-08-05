from typing import List

from fastapi import APIRouter, status, Response
from fastapi.params import Depends, Query

from src.application.model.value import CartItem
from src.application.usecase import GetItemsFromCartUseCase, AddItemToCartUseCase, UpdateItemInCartUseCase, \
    RemoveItemFromCartUseCase
from src.interface.api.dto.mapper import to_cart_item_response_list
from src.interface.api.dto.response.cart_item_response import CartItemResponse
from src.interface.dependency import get_get_items_from_cart_use_case, get_add_item_to_cart_use_case, \
    get_update_item_in_cart_use_case, get_remove_item_from_cart_use_case
from src.interface.security import get_authentication_principal

router = APIRouter(
    prefix='/cart',
    tags=['Корзина товаров'],
    responses={
        401: {'description': 'Пользователь не аутентифицирован'}
    }
)


@router.get(
    '',
    summary='Получить товары из корзины',
    description='Получается товар из корзины текущего пользователя',
    responses={
        200: {'description': 'Товары из корзины'},
        204: {'description': 'Корзина пустая'},
    }
)
async def get_items(
        response: Response,
        port: GetItemsFromCartUseCase = Depends(get_get_items_from_cart_use_case),
        user_id: int = Depends(get_authentication_principal)
) -> List[CartItemResponse] | None:
    items = await port.execute(user_id)

    if len(items) == 0:
        response.status_code = status.HTTP_204_NO_CONTENT
        return None

    return to_cart_item_response_list(items)


@router.post(
    '',
    summary='Добавить товар в корзину',
    description='Добавляет товар в корзину текущего пользователя',
    responses={
        200: {'description': 'Товар добавлен в корзину', 'content': None},
        404: {'description': 'Товар не найден'},
        409: {'description': 'Товар уже добавлен в корзину'},
    }
)
async def add_item(
        product_id: int = Query(gt=0, description='Идентификатор товара'),
        quantity: int = Query(gt=0, description='Кол-во товара'),
        port: AddItemToCartUseCase = Depends(get_add_item_to_cart_use_case),
        user_id: int = Depends(get_authentication_principal)
) -> None:
    await port.execute(user_id=user_id,
                       new_item=CartItem(product_id=product_id, quantity=quantity))


@router.put(
    '',
    summary='Обновить товар в корзине',
    description='Обновляет товар в корзине текущего пользователя',
    responses={
        200: {'description': 'Товар в корзине обновлен', 'content': None},
    }
)
async def update_item(
        product_id: int = Query(gt=0, description='Идентификатор товара'),
        quantity: int = Query(gt=0, description='Новое кол-во товара'),
        port: UpdateItemInCartUseCase = Depends(get_update_item_in_cart_use_case),
        user_id: int = Depends(get_authentication_principal)
) -> None:
    await port.execute(user_id=user_id,
                       updated_item=CartItem(product_id=product_id, quantity=quantity))


@router.delete(
    '',
    summary='Удалить товар из корзины',
    description='Удаляет товар из корзины текущего пользователя',
    responses={
        200: {'description': 'Товар удален из корзины'},
    }
)
async def remove_item(
        product_id: int = Query(gt=0, description='Идентификатор товара'),
        port: RemoveItemFromCartUseCase = Depends(get_remove_item_from_cart_use_case),
        user_id: int = Depends(get_authentication_principal)
) -> None:
    await port.execute(user_id=user_id, product_id=product_id)
