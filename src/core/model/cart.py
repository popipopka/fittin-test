from dataclasses import dataclass, field
from typing import List, Optional

from src.core.error import RecordAlreadyExistsError, RecordNotFoundError
from src.core.model.value import CartItem


@dataclass(eq=False)
class Cart:
    user_id: int
    id: Optional[int] = None

    items: List[CartItem] = field(default_factory=list)

    def add_item(self, new_item: CartItem) -> None:
        for item in self.items:
            if item.product_id == new_item.product_id:
                raise RecordAlreadyExistsError.cart_item(self.id, new_item.product_id)

        self.items.append(new_item)

    def update_item(self, updated_item: CartItem) -> None:
        for i, item in enumerate(self.items):
            if item.product_id == updated_item.product_id:
                self.items[i] = updated_item
                return
                
        raise RecordNotFoundError.cart_item(self.id, updated_item.product_id)

    def remove_item_by_product_id(self, product_id: int) -> None:
        for i, item in enumerate(self.items):
            if item.product_id == product_id:
                del self.items[i]
                return

        raise RecordNotFoundError.cart_item(self.id, product_id)

    def empty(self) -> None:
        self.items = []

    def __eq__(self, other):
        if not isinstance(other, Cart):
            return False
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
