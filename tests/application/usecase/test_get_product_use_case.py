import unittest
from decimal import Decimal
from unittest.mock import MagicMock

from src.application.usecase.get_product_use_case import GetProductUseCase
from src.core.model import Product


class TestGetProductUseCase(unittest.TestCase):
    def setUp(self):
        self.product_repo = MagicMock()
        self.use_case = GetProductUseCase(self.product_repo)

    def test_execute(self):
        # Given
        expected = Product(1, 1, 'name1', 'desc1', Decimal('1'))

        self.product_repo.get_by_id.return_value = expected
        # When
        actual = self.use_case.execute(1)

        # Then
        self.product_repo.get_by_id.assert_called_once_with(1)

        self.assertEqual(expected, actual)