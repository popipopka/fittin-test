from typing import Optional, List

from fastapi import APIRouter, Response, status
from fastapi.params import Query, Depends, Path

from src.application.usecase import GetProductsUseCase, GetProductUseCase
from src.interface.api.dto.mapper import to_product_response, to_product_item_response_list
from src.interface.api.dto.request import GetProductsRequest
from src.interface.api.dto.response import ProductResponse
from src.interface.api.dto.response.product_item_response import ProductItemResponse
from src.interface.dependency import get_get_products_use_case, get_get_product_use_case

router = APIRouter(
    tags=['Товары']
)


@router.post(
    '/products',
    summary='Получить список товаров в категории',
    description='Получает список товаров в заданной категории',
    responses={
        200: {'description': 'Список товаров'},
        204: {'description': 'В категории нет товаров'},
        404: {'description': 'Заданная категория не найдена'}
    }
)
async def get_products(
        response: Response,
        body: Optional[GetProductsRequest] = None,
        category_id: int = Query(gt=0, description='Идентификатор категории'),
        input_port: GetProductsUseCase = Depends(get_get_products_use_case)
) -> List[ProductItemResponse] | None:
    products = await input_port.execute(category_id, body)

    if len(products) == 0:
        response.status_code = status.HTTP_204_NO_CONTENT
        return None

    return to_product_item_response_list(products)


@router.get(
    '/product/{product_id}',
    summary='Получить товар',
    description='Получает товар по идентификатору',
    responses={
        200: {'description': 'Товар'},
        404: {'description': 'Товар не найден'}
    }
)
async def get_product(
        product_id: int = Path(..., gt=0, description='Идентификатор товара'),
        input_port: GetProductUseCase = Depends(get_get_product_use_case),
) -> ProductResponse:
    product = await input_port.execute(product_id)

    return to_product_response(product)
