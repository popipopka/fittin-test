from abc import ABC, abstractmethod

from src.core.model import Product


class GetProductPort(ABC):
    @abstractmethod
    async def execute(self, product_id: int) -> Product:
        pass
