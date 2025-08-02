from decimal import Decimal
from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock

from src.application.usecase.get_product_use_case import GetProductUseCase
from src.core.error import RecordNotFoundError
from src.core.model import Product


class TestGetProductUseCase(IsolatedAsyncioTestCase):
    def setUp(self):
        self.product_repo = AsyncMock()
        self.product_image_repo = AsyncMock()
        self.use_case = GetProductUseCase(self.product_repo, self.product_image_repo)

    async def test_execute_success(self):
        # Given
        expected = Product(1, 1, 'name1', 'desc1', Decimal('1'))

        self.product_repo.get_by_id.return_value = expected
        # When
        actual = await self.use_case.execute(1)

        # Then
        self.product_repo.get_by_id.assert_called_once_with(1)
        self.product_image_repo.get_image_url_by_product_id.assert_called_once_with(1)

        self.assertEqual(expected, actual)

    async def test_execute_product_not_found_raises(self):
        # Given
        self.product_repo.get_by_id.return_value = None

        # When. Then
        with self.assertRaises(RecordNotFoundError) as context:
            await self.use_case.execute(999)

        self.product_repo.get_by_id.assert_called_once_with(999)
        self.product_image_repo.get_image_url_by_product_id.assert_not_called()

        self.assertEqual(
            'Product with id 999 not found',
            str(context.exception)
        )
