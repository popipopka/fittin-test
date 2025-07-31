from abc import ABC, abstractmethod
from typing import List, Optional

from src.core.model import Product, Cart
from src.core.model.value import CartItem


class CartRepository(ABC):
    @abstractmethod
    async def get_items_by_user_id(self, user_id: int) -> List[CartItem]:
        pass

    @abstractmethod
    async def get_cart_by_user_id(self, user_id: int) -> Optional[Cart]:
        pass

    @abstractmethod
    async def save(self, cart: Cart) -> int:
        pass