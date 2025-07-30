from typing import List, Dict

from src.core.model import Product
from src.core.model.value import CartItem, OrderItem
from src.core.shared.result.cart_item_data import CartItemData
from src.core.shared.result.product_item_data import ProductItemData


def to_product_item_data_list(products: List[Product], image_urls: Dict[int, str]) -> List[ProductItemData]:
    return [ProductItemData(id=product.id,
                            name=product.name,
                            price=product.price,
                            image_url=image_urls[product.id])
            for product in products]


def to_cart_item_data_list(cart_items: List[CartItem], products: List[Product], image_urls: Dict[int, str]) -> List[
    CartItemData]:
    product_items = to_product_item_data_list(products, image_urls)
    quantities = {item.product_id: item.quantity for item in cart_items}

    return [CartItemData(product=product_item,
                         quantity=quantities[product_item.id])
            for product_item in product_items]


def to_order_item_list(cart_items: List[CartItem], products: List[Product]) -> List[OrderItem]:
    quantities = {item.product_id: item.quantity for item in cart_items}

    return [OrderItem(product_id=product.id,
                      unit_price=product.price,
                      quantity=quantities[product.id])
            for product in products]
