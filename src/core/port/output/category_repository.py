from abc import ABC, abstractmethod
from typing import List

from src.core.model import Category


class CategoryRepository(ABC):
    @abstractmethod
    async def get_all(self) -> List[Category]:
        pass

    @abstractmethod
    async def exists(self, id: int) -> bool:
        pass