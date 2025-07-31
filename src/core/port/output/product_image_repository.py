from abc import ABC, abstractmethod
from typing import List, Dict


class ProductImageRepository(ABC):
    @abstractmethod
    async def get_image_urls_by_product_ids(self, product_ids: List[int]) -> Dict[int, str]:
        pass