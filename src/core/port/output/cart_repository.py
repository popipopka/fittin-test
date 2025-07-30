from abc import ABC, abstractmethod
from typing import List

from src.core.model import Product, Cart
from src.core.model.value import CartItem


class CartRepository(ABC):
    @abstractmethod
    def get_items_by_user_id(self, user_id: int) -> List[CartItem]:
        pass

    @abstractmethod
    def get_cart_by_user_id(self, user_id: int) -> Cart:
        pass

    @abstractmethod
    def save(self, cart: Cart) -> None:
        pass