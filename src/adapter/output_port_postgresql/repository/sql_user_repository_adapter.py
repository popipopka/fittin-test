from sqlalchemy import select, exists
from sqlalchemy.ext.asyncio import AsyncSession

from src.adapter.output_port_postgresql.entity import UserEntity
from src.core.port.output.user_repository import UserRepository


class SqlUserRepositoryAdapter(UserRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def exists_by_id(self, user_id: int) -> bool:
        result = await self.session.execute(
            select(exists().where(UserEntity.id == user_id))
        )
        return result.scalar()