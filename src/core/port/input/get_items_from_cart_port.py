from abc import ABC, abstractmethod
from typing import List

from src.core.shared.result import CartItemData


class GetItemsFromCartPort(ABC):
    @abstractmethod
    async def execute(self, user_id: int) -> List[CartItemData]:
        pass
