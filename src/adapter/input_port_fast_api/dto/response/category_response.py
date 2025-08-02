from typing import List

from pydantic import BaseModel, Field


class CategoryResponse(BaseModel):
    id: int = Field(description='Уникальный идентификатор', examples=[2])
    name: str = Field(description='Название категории', examples=['Меховые изделия'])

    children: List['CategoryResponse'] = Field(
        description='Список дочерних категорий',
        examples=[{
            'id': 3,
            'name': 'Норковые изделия',
            'children': []
        }]
    )


CategoryResponse.model_rebuild()
