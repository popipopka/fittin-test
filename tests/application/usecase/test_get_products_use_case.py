from decimal import Decimal
from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock

from src.application.usecase.get_products_use_case import GetProductsUseCase
from src.core.model import Product
from src.core.shared.params import ProductFilterParams
from src.core.shared.result.product_item_data import ProductItemData


class TestGetProductsUseCase(IsolatedAsyncioTestCase):
    def setUp(self):
        self.product_repo = AsyncMock()
        self.product_image_repo = AsyncMock()
        self.use_case = GetProductsUseCase(self.product_repo, self.product_image_repo)

        self.products = [
            Product(1, 1, 'name1', 'desc1', Decimal('50')),
            Product(2, 1, 'name2', 'desc2', Decimal('80')),
        ]
        self.image_urls = {1: 'url1', 2: 'url2'}
        self.expected = [
            ProductItemData(1, 'name1', Decimal('50'), 'url1'),
            ProductItemData(2, 'name2', Decimal('80'), 'url2'),
        ]

    async def test_execute_with_filters(self):
        # Given
        filters = ProductFilterParams(min_price=Decimal('10'), max_price=Decimal('100'))

        self.product_repo.get_all.return_value = self.products
        self.product_image_repo.get_image_urls_by_product_ids.return_value = self.image_urls

        # When
        actual = await self.use_case.execute(category_id=1, filters=filters)

        # Then
        self.product_repo.get_all.assert_called_once_with(filters)
        self.product_image_repo.get_image_urls_by_product_ids.assert_called_once_with([1, 2])

        self.assertEqual(self.expected, actual)

    async def test_execute_without_filters(self):
        # Given
        self.product_repo.get_all.return_value = self.products
        self.product_image_repo.get_image_urls_by_product_ids.return_value = self.image_urls

        # When
        actual = await self.use_case.execute(category_id=1)

        # Then
        self.product_repo.get_all.assert_called_once_with(ProductFilterParams())
        self.product_image_repo.get_image_urls_by_product_ids.assert_called_once_with([1, 2])

        self.assertEqual(self.expected, actual)