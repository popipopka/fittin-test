from typing import List

from src.application.shared.result import CartItemData
from src.interface.api.dto.response.cart_item_response import CartItemResponse
from .product_mapper import to_product_item_response


def to_cart_item_response_list(cart_item_data_list: List[CartItemData]) -> List[CartItemResponse]:
    return list(map(__to_cart_item_response, cart_item_data_list))


def __to_cart_item_response(cart_item_data: CartItemData) -> CartItemResponse:
    return CartItemResponse(
        product=to_product_item_response(cart_item_data.product),
        quantity=cart_item_data.quantity,
    )
