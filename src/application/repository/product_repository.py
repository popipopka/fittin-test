from abc import ABC, abstractmethod
from typing import List, Optional

from src.application.model import Product
from src.application.shared.params import ProductFilterParams


class ProductRepository(ABC):
    @abstractmethod
    async def get_by_id(self, product_id: int) -> Optional[Product]:
        pass

    @abstractmethod
    async def get_all_by_category_id(self, category_id: int, filters: ProductFilterParams) -> List[Product]:
        pass

    @abstractmethod
    async def get_all_by_ids(self, ids: List[int]) -> List[Product]:
        pass

    @abstractmethod
    async def exists_by_id(self, product_id: int) -> bool:
        pass