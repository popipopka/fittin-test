import unittest
from decimal import Decimal
from typing import List

from parameterized import parameterized

from src.core.error import RecordAlreadyExistsError
from src.core.model import Order
from src.core.model.value import OrderItem


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.order = Order(1, 1)
        self.item1 = OrderItem(1, Decimal('1'), 1)
        self.item2 = OrderItem(2, Decimal('2'), 2)

    @parameterized.expand([
        ('no_item', [], Decimal("0")),
        ('one_item', [OrderItem(1, quantity=2, unit_price=Decimal("5"))], Decimal("10")),
        ('multiple_items', [
            OrderItem(1, quantity=2, unit_price=Decimal("5.2")),
            OrderItem(2, quantity=1, unit_price=Decimal("7.5")),
            OrderItem(3, quantity=3, unit_price=Decimal("2"))
        ], Decimal("10.4") + Decimal("7.5") + Decimal("6")),
    ])
    def test_total_price(self, test_label, items: List[OrderItem], expected_total_price: Decimal):
        # Given
        self.order.add_items(items)

        # When
        actual_total_price: Decimal = self.order.total_price

        # Then
        self.assertEqual(expected_total_price, actual_total_price)

    def test_add_items_success(self):
        # Given
        # When
        self.order.add_items([self.item1, self.item2])

        # Then
        self.assertIn(self.item1, self.order.items)
        self.assertIn(self.item2, self.order.items)

    def test_add_item_already_exists_raises(self):
        # Given
        self.order.add_items([self.item1, self.item2])

        # When, Then
        with self.assertRaises(RecordAlreadyExistsError) as context:
            self.order.add_items([self.item1])

        self.assertEqual(
            f'Product with id={self.item1.product_id} already exists in order with id={self.order.id}',
            str(context.exception)
        )

    def test_equality(self):
        # Given
        first = Order(1, 2)
        second = Order(1, 4)

        # When, Then
        self.assertEqual(first, second)

    def test_inequality(self):
        # Given
        first = Order(1, 2)
        second = Order(2, 4)

        # When, Then
        self.assertNotEqual(first, second)
