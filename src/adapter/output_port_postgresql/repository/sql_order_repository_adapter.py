from sqlalchemy.ext.asyncio import AsyncSession

from src.adapter.output_port_postgresql.repository.mapper import to_order_entity
from src.core.model import Order
from src.core.port.output.order_repository import OrderRepository


class SqlOrderRepositoryAdapter(OrderRepository):

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
