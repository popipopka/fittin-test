from abc import ABC, abstractmethod
from typing import List

from src.core.model import Product
from src.core.shared.params import ProductFilterParams


class ProductRepository(ABC):
    @abstractmethod
    def get_by_id(self, product_id: int) -> Product:
        pass

    @abstractmethod
    def get_all(self, filters: ProductFilterParams) -> List[Product]:
        pass

    @abstractmethod
    def get_all_by_ids(self, ids: List[int]) -> List[Product]:
        pass