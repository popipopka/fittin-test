from abc import ABC, abstractmethod

from src.core.model.value import CartItem


class AddItemToCartPort(ABC):
    @abstractmethod
    def execute(self, user_id: int, item: CartItem) -> None:
        pass
