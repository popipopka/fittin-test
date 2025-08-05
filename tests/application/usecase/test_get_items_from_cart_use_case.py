from decimal import Decimal
from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock

from src.application.error import RecordNotFoundError
from src.application.model import Product
from src.application.model.value import CartItem
from src.application.shared.result import CartItemData, ProductItemData
from src.application.usecase import GetItemsFromCartUseCase


class TestGetItemsFromCartUseCase(IsolatedAsyncioTestCase):
    def setUp(self):
        self.cart_repo = AsyncMock()
        self.user_repo = AsyncMock()
        self.product_repo = AsyncMock()
        self.product_image_repo = AsyncMock()

        self.use_case = GetItemsFromCartUseCase(self.cart_repo, self.user_repo, self.product_repo,
                                                self.product_image_repo)

    async def test_execute_success(self):
        # Given
        user_id = 1

        cart_items = [
            CartItem(1, 1),
            CartItem(2, 2),
        ]
        products = [
            Product(1, 1, 'name1', 'desc1', Decimal('1')),
            Product(2, 1, 'name2', 'desc2', Decimal('2')),
        ]
        image_urls = {1: 'url1', 2: 'url2'}

        expected = [
            CartItemData(ProductItemData(1, 'name1', Decimal('1'), 'url1'), 1),
            CartItemData(ProductItemData(2, 'name2', Decimal('2'), 'url2'), 2),
        ]

        self.user_repo.exists_by_id.return_value = True
        self.cart_repo.get_items_by_user_id.return_value = cart_items
        self.product_repo.get_all_by_ids.return_value = products
        self.product_image_repo.get_image_urls_by_product_ids.return_value = image_urls

        # When
        actual = await self.use_case.execute(user_id)

        # Then
        self.assertEqual(expected, actual)

        self.user_repo.exists_by_id.assert_called_once_with(user_id)
        self.cart_repo.get_items_by_user_id.assert_called_once_with(user_id)
        self.product_repo.get_all_by_ids.assert_called_once_with([1, 2])
        self.product_image_repo.get_image_urls_by_product_ids.assert_called_once_with([1, 2])

    async def test_execute_user_not_found_raises(self):
        # Given
        user_id = 1

        self.user_repo.exists_by_id.return_value = False

        # When, Then
        with self.assertRaises(RecordNotFoundError) as context:
            await self.use_case.execute(user_id)

        self.assertEqual(f'User with id {user_id} not found', str(context.exception))

        self.user_repo.exists_by_id.assert_called_once_with(user_id)

        self.cart_repo.get_cart_by_user_id.assert_not_called()
        self.product_repo.get_all_by_ids.assert_not_called()
        self.product_image_repo.get_image_urls_by_product_ids.assert_not_called()
        self.cart_repo.save.assert_not_called()
