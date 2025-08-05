import unittest
from decimal import Decimal

from parameterized import parameterized

from src.application.model.value import OrderItem


class TestOrderItem(unittest.TestCase):

    @parameterized.expand([
        (OrderItem(1, quantity=1, unit_price=Decimal('10')), Decimal('10')),
        (OrderItem(1, quantity=2, unit_price=Decimal('5.5')), Decimal('11')),
        (OrderItem(1, quantity=3, unit_price=Decimal('21.333')), Decimal('63.999')),
    ])
    def test_total_price(self, order_item: OrderItem, expected_total_price: Decimal) -> None:
        # Given
        # When
        actual_total_price: Decimal = order_item.total_price
        # Then
        self.assertEqual(actual_total_price, expected_total_price)
