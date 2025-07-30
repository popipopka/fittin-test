from abc import ABC, abstractmethod
from typing import List, Dict


class ProductImageRepository(ABC):
    @abstractmethod
    def get_image_urls_by_product_ids(self, product_ids: List[int]) -> Dict[int, str]:
        pass