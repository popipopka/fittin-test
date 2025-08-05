from typing import List

from sqlalchemy import select, exists
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.model import Category
from src.application.repository import CategoryRepository
from src.infrastructure.database.entity import CategoryEntity
from src.infrastructure.database.repository.mapper import to_category_model_list


class SqlCategoryRepository(CategoryRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> List[Category]:
        result = await self.session.execute(
            select(CategoryEntity)
            .order_by(CategoryEntity.name.asc())
        )
        categories = result.scalars().all()

        return to_category_model_list(categories)

    async def exists(self, id: int):
        result = await self.session.execute(
            select(exists().where(CategoryEntity.id == id))
        )
        return result.scalar()
