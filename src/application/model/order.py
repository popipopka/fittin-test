from dataclasses import dataclass, field
from datetime import datetime, timezone
from decimal import Decimal
from typing import List, Optional

from src.application.error import RecordAlreadyExistsError
from src.application.model.value import OrderItem


@dataclass(eq=False)
class Order:
    user_id: int
    id: Optional[int] = None

    items: List[OrderItem] = field(default_factory=list, init=False)

    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc), init=False)

    @property
    def total_price(self) -> Decimal:
        return sum((item.total_price for item in self.items), Decimal('0'))

    def add_items(self, new_items: List[OrderItem]) -> 'Order':
        existing_product_ids = {item.product_id for item in self.items}

        for new_item in new_items:
            if new_item.product_id in existing_product_ids:
                raise RecordAlreadyExistsError.order_item(self.id, new_item.product_id)

            self.items.append(new_item)
            existing_product_ids.add(new_item.product_id)

        return self

    def __eq__(self, other):
        if not isinstance(other, Order):
            return False
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
