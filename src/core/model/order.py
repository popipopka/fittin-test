from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from typing import List, Optional

from src.core.error import RecordAlreadyExistsError
from src.core.model.value import OrderItem


@dataclass(eq=False)
class Order:
    id: int
    user_id: int

    items: List[OrderItem] = field(default_factory=list)

    created_at: datetime = field(default_factory=datetime.now)

    @property
    def total_price(self) -> Decimal:
        return sum((item.total_price for item in self.items), Decimal('0'))

    def add_item(self, new_item: OrderItem) -> None:
        for i, item in enumerate(self.items):
            if item.product_id == new_item.product_id:
                raise RecordAlreadyExistsError.order_item(self.id, new_item.product_id)

        self.items.append(new_item)

    def __eq__(self, other):
        if not isinstance(other, Order):
            return False
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
