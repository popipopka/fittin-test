from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

from .sort_direction import SortDirection


@dataclass
class ProductFilterParams:
    min_price: Optional[Decimal] = None
    max_price: Optional[Decimal] = None

    price_sort_direction: Optional[SortDirection] = None
