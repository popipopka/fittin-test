from abc import ABC, abstractmethod

from src.core.model.value import CartItem


class UpdateItemInCartPort(ABC):
    @abstractmethod
    def execute(self, user_id: int, updated_item: CartItem) -> None:
        pass
