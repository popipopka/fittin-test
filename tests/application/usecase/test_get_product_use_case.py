from decimal import Decimal
from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock

from src.application.usecase.get_product_use_case import GetProductUseCase
from src.core.model import Product


class TestGetProductUseCase(IsolatedAsyncioTestCase):
    def setUp(self):
        self.product_repo = AsyncMock()
        self.use_case = GetProductUseCase(self.product_repo)

    async def test_execute(self):
        # Given
        expected = Product(1, 1, 'name1', 'desc1', Decimal('1'))

        self.product_repo.get_by_id.return_value = expected
        # When
        actual = await self.use_case.execute(1)

        # Then
        self.product_repo.get_by_id.assert_called_once_with(1)

        self.assertEqual(expected, actual)