from typing import List

from src.adapter.input_port_fast_api.dto.response.category_response import CategoryResponse
from src.core.shared.result import CategoryData


def category_data_list_to_response(category: List[CategoryData]) -> List[CategoryResponse]:
    return list(map(__category_data_to_response, category))

def __category_data_to_response(category: CategoryData) -> CategoryResponse:
    return CategoryResponse(
        id=category.id,
        name=category.name,
        children=[__category_data_to_response(child) for child in category.children]
    )