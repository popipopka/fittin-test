from dataclasses import dataclass
from decimal import Decimal


@dataclass
class ProductItemData:
    id: int
    name: str
    price: Decimal

    image_url: str