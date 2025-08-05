from typing import List, Dict

from src.application.model import Product
from src.application.model.value import CartItem
from src.application.shared.result import CartItemData
from .product_mapper import to_product_item_data_list


def to_cart_item_data_list(
        cart_items: List[CartItem], products: List[Product], image_urls: Dict[int, str]
) -> List[CartItemData]:
    product_items = to_product_item_data_list(products, image_urls)
    quantities = {item.product_id: item.quantity for item in cart_items}

    return [CartItemData(product=product_item,
                         quantity=quantities[product_item.id])
            for product_item in product_items]
