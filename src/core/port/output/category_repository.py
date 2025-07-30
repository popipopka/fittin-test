from abc import ABC, abstractmethod
from typing import List

from src.core.model import Category


class CategoryRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Category]:
        pass