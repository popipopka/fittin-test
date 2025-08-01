from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.adapter.output_port_postgresql.entity import CartEntity
from src.adapter.output_port_postgresql.repository.mapper import to_cart_entity, to_cart_model, to_cart_item_model_list
from src.core.model import Cart
from src.core.model.value import CartItem
from src.core.port.output.cart_repository import CartRepository


class SqlCartRepository(CartRepository):

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_items_by_user_id(self, user_id: int) -> List[CartItem]:
        result = await self.session.execute(
            select(CartEntity)
            .where(CartEntity.user_id == user_id)
        )
        cart = result.unique().scalar_one()

        return to_cart_item_model_list(cart.items)

    async def get_cart_by_user_id(self, user_id: int) -> Optional[Cart]:
        result = await self.session.execute(
            select(CartEntity)
            .where(CartEntity.user_id == user_id)
        )
        cart = result.unique().scalar_one_or_none()

        return to_cart_model(cart)

    async def save(self, cart: Cart) -> int:
        entity = to_cart_entity(cart)

        if cart.id:
            await self.session.merge(entity)
        else:
            self.session.add(entity)

        await self.session.flush()
        return entity.id
