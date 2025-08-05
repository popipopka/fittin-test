from typing import List

from fastapi import APIRouter, Depends

from src.application.usecase import GetCategoriesUseCase
from src.interface.api.dto.mapper import category_data_list_to_response
from src.interface.api.dto.response import CategoryResponse
from src.interface.dependency import get_get_categories_use_case

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
        input_port: GetCategoriesUseCase = Depends(get_get_categories_use_case)
) -> List[CategoryResponse]:
    result = await input_port.execute()
    response_data = category_data_list_to_response(result)

    return response_data
