from abc import ABC, abstractmethod


class RemoveItemFromCartPort(ABC):
    @abstractmethod
    def execute(self, user_id: int, product_id: int) -> None:
        pass
