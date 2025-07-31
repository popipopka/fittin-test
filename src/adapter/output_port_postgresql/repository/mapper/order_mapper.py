from typing import List

from src.adapter.output_port_postgresql.entity import OrderEntity, OrderItemEntity
from src.core.model import Order
from src.core.model.value import OrderItem


def to_order_entity(order_model: Order) -> OrderEntity:
    entity = OrderEntity(
        user_id=order_model.user_id,
        created_at=order_model.created_at
    )
    if order_model.id:
        entity.id = order_model.id

    entity.items = __to_order_item_entity_list(order_model.items, order_model.id)

    return entity


def __to_order_item_entity_list(order_item_models: List[OrderItem], order_id: int) -> List[OrderItemEntity]:
    return [__to_order_item_entity(item, order_id)
            for item in order_item_models]


def __to_order_item_entity(order_item_model: OrderItem, order_id: int) -> OrderItemEntity:
    entity = OrderItemEntity(
        order_id=order_id,
        product_id=order_item_model.product_id,
        unit_price=order_item_model.unit_price,
        quantity=order_item_model.quantity,
    )
    if order_id:
        entity.id = order_id

    return entity
