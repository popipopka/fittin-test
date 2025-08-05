from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field

from src.application.shared.enum import SortDirection


class GetProductsRequest(BaseModel):
    min_price: Optional[Decimal] = Field(None, gt=0, description='Минимальная цена', examples=[300])
    max_price: Optional[Decimal] = Field(None, gt=0, description='Максимальная цена', examples=[9000])

    price_sort_direction: Optional[SortDirection] = Field(
        None,
        description='Направление сортировки по цене',
    )
