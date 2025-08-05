from sqlalchemy.ext.asyncio import AsyncSession

from src.application.model import Order
from src.application.repository import OrderRepository
from src.infrastructure.database.repository.mapper import to_order_entity


class SqlOrderRepository(OrderRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, order: Order) -> int:
        entity = to_order_entity(order)

        if order.id:
            await self.session.merge(entity)
        else:
            self.session.add(entity)

        await self.session.flush()
        return entity.id
