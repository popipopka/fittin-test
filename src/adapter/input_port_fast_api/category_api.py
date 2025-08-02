from typing import List

from fastapi import APIRouter, Depends

from src.adapter.input_port_fast_api.dependency import get_get_categories_port
from src.adapter.input_port_fast_api.dto.mapper import category_data_list_to_response
from src.adapter.input_port_fast_api.dto.response import CategoryResponse
from src.core.port.input import GetCategoriesPort

router = APIRouter(
    prefix='/categories',
    tags=['Категории'],
)


@router.get(
    '',
    summary='Получить список категорий',
    description='Получает список категорий с вложенностью',
    responses={
        200: {'description': 'Список категорий'},
    }
)
async def get_categories(
        input_port: GetCategoriesPort = Depends(get_get_categories_port)
) -> List[CategoryResponse]:
    result = await input_port.execute()
    response_data = category_data_list_to_response(result)

    return response_data
