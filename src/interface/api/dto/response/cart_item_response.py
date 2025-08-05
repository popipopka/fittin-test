from pydantic import BaseModel, Field

from src.interface.api.dto.response import ProductItemResponse


class CartItemResponse(BaseModel):
    product: ProductItemResponse = Field(description='Товар в корзине')
    quantity: int = Field(description='Кол-во товара в корзине', examples=[10])