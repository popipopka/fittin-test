from typing import List, Dict

from src.core.model import Product, Order
from src.core.model.value import CartItem, OrderItem
from src.core.shared.params import OrderCreatedNotificationParams
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


def to_order_created_notifications_params(
        user_email: str,
        order: Order,
        products: List[Product]
) -> OrderCreatedNotificationParams:
    return OrderCreatedNotificationParams(
        user_email=user_email,
        total_price=order.total_price,
        created_at=order.created_at,
        order_id=order.id,
        products=__to_order_created_product_item_list(products, order.items),
    )


def __to_order_created_product_item_list(
        products: List[Product], order_items: List[OrderItem]
) -> List[OrderCreatedNotificationParams.OrderCreatedProductItem]:
    product_name_map = {product.id: product.name for product in products}

    return [OrderCreatedNotificationParams.OrderCreatedProductItem(
        name=product_name_map[item.product_id],
        price=item.unit_price,
        quantity=item.quantity)
        for item in order_items]
