from abc import ABC, abstractmethod
from typing import List

from src.core.shared.result import CategoryData


class GetCategoriesPort(ABC):
    @abstractmethod
    async def execute(self) -> List[CategoryData]:
        pass
