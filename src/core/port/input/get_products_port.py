from abc import ABC, abstractmethod
from typing import Optional, List

from src.core.shared.params import ProductFilterParams
from src.core.shared.result.product_item_data import ProductItemData


class GetProductsPort(ABC):
    @abstractmethod
    def execute(self, category_id: int, filters: Optional[ProductFilterParams] = None) -> List[ProductItemData]:
        pass
