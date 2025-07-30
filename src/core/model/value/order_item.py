from dataclasses import dataclass, field
from decimal import Decimal


@dataclass(frozen=True)
class OrderItem:
    product_id: int
    unit_price: Decimal
    quantity: int = field(default=1)

    @property
    def total_price(self) -> Decimal:
        return self.unit_price * self.quantity