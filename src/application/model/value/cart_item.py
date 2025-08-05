from dataclasses import dataclass, field


@dataclass(frozen=True)
class CartItem:
    product_id: int
    quantity: int = field(default=1)
