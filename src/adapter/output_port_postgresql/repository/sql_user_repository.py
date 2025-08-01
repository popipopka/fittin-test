from typing import Optional

from sqlalchemy import select, exists
from sqlalchemy.ext.asyncio import AsyncSession

from src.adapter.output_port_postgresql.entity import UserEntity
from src.adapter.output_port_postgresql.repository.mapper import to_user_entity, to_user_model
from src.core.model import User
from src.core.port.output.user_repository import UserRepository


class SqlUserRepository(UserRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def exists_by_id(self, user_id: int) -> bool:
        result = await self.session.execute(
            select(exists().where(UserEntity.id == user_id))
        )
        return result.scalar()

    async def exists_by_email(self, email: str) -> bool:
        result = await self.session.execute(
            select(exists().where(UserEntity.email == email))
        )
        return result.scalar()

    async def save(self, user: User) -> int:
        entity = to_user_entity(user)

        if user.id:
            await self.session.merge(entity)
        else:
            self.session.add(entity)

        await self.session.flush()
        return entity.id

    async def get_by_email(self, email: str) -> Optional[User]:
        result = await self.session.execute(
            select(UserEntity)
            .where(UserEntity.email == email)
        )
        user = result.scalar_one_or_none()

        return to_user_model(user)
