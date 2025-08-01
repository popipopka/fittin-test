from typing import Optional

from sqlalchemy import select, exists
from sqlalchemy.ext.asyncio import AsyncSession

from src.adapter.output_port_postgresql.entity import RefreshTokenEntity
from src.adapter.output_port_postgresql.repository.mapper import to_refresh_token_entity, to_refresh_token_model
from src.core.model.refresh_token import RefreshToken
from src.core.port.output import RefreshTokenRepository


class SqlRefreshTokenRepository(RefreshTokenRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, token: RefreshToken) -> int:
        entity = to_refresh_token_entity(token)

        if token.id:
            await self.session.merge(entity)
        else:
            self.session.add(entity)

        await self.session.flush()
        return entity.id

    async def get_by_user_id(self, user_id: int) -> Optional[RefreshToken]:
        result = await self.session.execute(
            select(RefreshTokenEntity)
            .where(RefreshTokenEntity.user_id == user_id)
        )
        user = result.scalar_one_or_none()

        return to_refresh_token_model(user)

    async def exists_by_user_id(self, user_id: int) -> bool:
        result = await self.session.execute(
            select(exists().where(RefreshTokenEntity.user_id == user_id))
        )
        return result.scalar()
