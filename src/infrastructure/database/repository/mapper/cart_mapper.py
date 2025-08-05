from typing import List, Optional

from src.application.model import Cart
from src.application.model.value import CartItem
from src.infrastructure.database.entity import CartEntity, CartItemEntity


def to_cart_model(cart_entity: CartEntity) -> Optional[Cart]:
    if not cart_entity:
        return None

    return Cart(
        id=cart_entity.id,
        user_id=cart_entity.user_id,
        items=to_cart_item_model_list(cart_entity.items),
    )


def to_cart_item_model_list(cart_item_entities: List[CartItemEntity]) -> List[CartItem]:
    return list(map(__to_cart_item_model, cart_item_entities))


def __to_cart_item_model(cart_item_entity: CartItemEntity) -> CartItem:
    return CartItem(
        product_id=cart_item_entity.product_id,
        quantity=cart_item_entity.quantity,
    )


def to_cart_entity(cart_model: Cart) -> CartEntity:
    entity = CartEntity(
        id=cart_model.id,
        user_id=cart_model.user_id,
    )
    if cart_model.id:
        entity.id = cart_model.id
    entity.items = __to_cart_item_entity_list(cart_model.items, cart_model.id)

    return entity


def __to_cart_item_entity_list(cart_item_models: List[CartItem], cart_id: int) -> List[CartItemEntity]:
    return [__to__cart_item_entity(item, cart_id)
            for item in cart_item_models]


def __to__cart_item_entity(cart_item_model: CartItem, cart_id: int) -> CartItemEntity:
    entity = CartItemEntity(
        product_id=cart_item_model.product_id,
        quantity=cart_item_model.quantity,
    )
    if cart_id:
        entity.id = cart_id

    return entity
