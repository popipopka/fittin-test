from typing import Optional, List

from fastapi import APIRouter, Response, status
from fastapi.params import Query, Depends, Path

from src.adapter.input_port_fast_api.dependency import get_get_products_port, get_get_product_port
from src.adapter.input_port_fast_api.dto.mapper import to_product_item_response_list
from src.adapter.input_port_fast_api.dto.mapper.product_mapper import to_product_response
from src.adapter.input_port_fast_api.dto.request import GetProductsRequest
from src.adapter.input_port_fast_api.dto.response import ProductResponse
from src.adapter.input_port_fast_api.dto.response.product_item_response import ProductItemResponse
from src.core.port.input import GetProductsPort, GetProductPort

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
        input_port: GetProductsPort = Depends(get_get_products_port)
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
        input_port: GetProductPort = Depends(get_get_product_port),
) -> ProductResponse:
    product = await input_port.execute(product_id)

    return to_product_response(product)