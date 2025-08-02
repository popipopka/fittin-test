from typing import List, Optional

from sqlalchemy import select, Select, exists
from sqlalchemy.ext.asyncio import AsyncSession

from src.adapter.output_port_postgresql.entity import ProductEntity
from src.adapter.output_port_postgresql.repository.mapper import to_product_model, to_product_model_list
from src.core.model import Product
from src.core.port.output.product_repository import ProductRepository
from src.core.shared.params import ProductFilterParams, SortDirection


class SqlProductRepository(ProductRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, product_id: int) -> Optional[Product]:
        product = await self.session.get(ProductEntity, product_id)

        return to_product_model(product)

    async def get_all_by_category_id(self, category_id: int, filters: ProductFilterParams) -> List[Product]:
        result = await self.session.execute(
            apply_filters(select(ProductEntity), filters)
            .where(ProductEntity.category_id == category_id)
        )
        products = result.scalars().all()

        return to_product_model_list(products)

    async def get_all_by_ids(self, ids: List[int]) -> List[Product]:
        result = await self.session.execute(
            select(ProductEntity)
            .where(ProductEntity.id.in_(ids))
        )
        products = result.scalars().all()

        return to_product_model_list(products)

    async def exists_by_id(self, product_id: int) -> bool:
        result = await self.session.execute(
            select(exists().where(ProductEntity.id == product_id))
        )
        return result.scalar()


def apply_filters(stmt: Select, filters: ProductFilterParams) -> Select:
    if filters.min_price:
        stmt = stmt.where(ProductEntity.price >= filters.min_price)

    if filters.max_price:
        stmt = stmt.where(ProductEntity.price <= filters.max_price)

    if filters.price_sort_direction == SortDirection.ASC:
        stmt = stmt.order_by(ProductEntity.price.asc())
    elif filters.price_sort_direction == SortDirection.DESC:
        stmt = stmt.order_by(ProductEntity.price.desc())

    return stmt
