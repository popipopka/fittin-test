from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import List


@dataclass
class OrderCreatedNotificationParams:
    user_email: str

    order_id: int
    products: List['OrderCreatedProductItem']
    total_price: Decimal
    created_at: datetime

    @dataclass
    class OrderCreatedProductItem:
        name: str
        price: Decimal
        quantity: int
