from dataclasses import dataclass, field
from datetime import datetime, timezone
from decimal import Decimal
from typing import List

from src.application.model.value import Attribute


@dataclass(eq=False)
class Product:
    id: int
    category_id: int

    name: str
    description: str
    price: Decimal
    image_url: str = field(repr=False, init=False)

    attributes: List[Attribute] = field(default_factory=list)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
