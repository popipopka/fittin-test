from typing import List

from src.application.model import Product, Order
from src.application.model.value import OrderItem, CartItem
from src.application.shared.params import OrderCreatedNotificationParams


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
