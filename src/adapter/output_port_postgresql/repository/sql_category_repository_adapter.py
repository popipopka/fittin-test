from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.adapter.output_port_postgresql.entity import CategoryEntity
from src.adapter.output_port_postgresql.repository.mapper import to_category_model_list
from src.core.model import Category
from src.core.port.output.category_repository import CategoryRepository


class SqlCategoryRepositoryAdapter(CategoryRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> List[Category]:
        result = await self.session.execute(
            select(CategoryEntity)
            .order_by(CategoryEntity.name.asc())
        )
        categories = result.scalars().all()

        return to_category_model_list(categories)