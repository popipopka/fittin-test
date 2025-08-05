from decimal import Decimal
from typing import List

from pydantic import BaseModel, Field


class AttributeResponse(BaseModel):
    name: str = Field(description='Название аттрибута', examples=['Размер'])
    value: str = Field(description='Значение аттрибута', examples=['XXL'])

class ProductResponse(BaseModel):
    id: int = Field(description='Идентификатор товара', examples=[1])
    category_id: int = Field(description='Идентификатор категории товара', examples=[3])

    name: str = Field(description='Название товара', examples=['Шуба'])
    description: str = Field(description='Описание товара', examples=['Красивая'])
    price: Decimal = Field(description='Цена товара', examples=[9999.99])
    image_url: str = Field(description='Ссылка на изображение товара', examples=['https://img.url'])

    attributes: List[AttributeResponse] = Field(description='Аттрибуты товара')