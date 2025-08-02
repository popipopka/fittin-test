from abc import ABC, abstractmethod

from src.core.model.value import CartItem


class AddItemToCartPort(ABC):
    @abstractmethod
    async def execute(self, user_id: int, new_item: CartItem) -> None:
        pass
