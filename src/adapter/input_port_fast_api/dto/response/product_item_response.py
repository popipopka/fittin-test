from decimal import Decimal

from pydantic import BaseModel, Field


class ProductItemResponse(BaseModel):
    id: int = Field(description='Идентификатор товара')
    name: str = Field(description='Название товара')
    price: Decimal = Field(description='Цена товара')

    image_url: str = Field(description='Ссылка на изображение товара')