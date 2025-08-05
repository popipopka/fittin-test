import unittest
from decimal import Decimal

from src.application.model import Product


class TestProduct(unittest.TestCase):
    def test_equality(self):
        # Given
        first = Product(1, 1, 'name', 'description', Decimal('0'))
        second = Product(1, 2, 'name2', 'description2', Decimal('2'))

        # When, Then
        self.assertEqual(first, second)

    def test_inequality(self):
        # Given
        first = Product(1, 1, 'name', 'description', Decimal('0'))
        second = Product(2, 1, 'name2', 'description', Decimal('1'))

        # When, Then
        self.assertNotEqual(first, second)