from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock

from src.application.error import RecordNotFoundError, RecordAlreadyExistsError
from src.application.model import Cart
from src.application.model.value import CartItem
from src.application.usecase import AddItemToCartUseCase


class TestAddItemToCartUseCase(IsolatedAsyncioTestCase):
    def setUp(self):
        self.cart_repo = AsyncMock()
        self.user_repo = AsyncMock()
        self.product_repo = AsyncMock()

        self.use_case = AddItemToCartUseCase(cart_repo=self.cart_repo,
                                             user_repo=self.user_repo,
                                             product_repo=self.product_repo)

        self.user_id = 1
        self.cart = Cart(1, self.user_id)
        self.item = CartItem(1, 1)

    async def test_execute_success(self):
        # Given
        self.user_repo.exists_by_id.return_value = True
        self.product_repo.exists_by_id.return_value = True
        self.cart_repo.get_cart_by_user_id.return_value = self.cart

        # When
        await self.use_case.execute(self.user_id, self.item)

        # Then
        self.user_repo.exists_by_id.assert_called_once_with(self.user_id)
        self.product_repo.exists_by_id.assert_called_once_with(self.item.product_id)
        self.cart_repo.get_cart_by_user_id.assert_called_once_with(self.user_id)
        self.cart_repo.save.assert_called_once()

    async def test_execute_user_not_found_raises(self):
        # Given
        self.user_repo.exists_by_id.return_value = False

        # When, Then
        with self.assertRaises(RecordNotFoundError) as context:
            await self.use_case.execute(self.user_id, self.item)

        self.assertEqual(f'User with id {self.user_id} not found', str(context.exception))

        self.user_repo.exists_by_id.assert_called_once_with(self.user_id)
        self.product_repo.exists_by_id.assert_not_called()
        self.cart_repo.get_cart_by_user_id.assert_not_called()
        self.cart_repo.save.assert_not_called()

    async def test_execute_product_not_found_raises(self):
        # Given
        self.user_repo.exists_by_id.return_value = True
        self.product_repo.exists_by_id.return_value = False

        # When, Then
        with self.assertRaises(RecordNotFoundError) as context:
            await self.use_case.execute(self.user_id, self.item)

        self.assertEqual(f'Product with id {self.user_id} not found', str(context.exception))

        self.user_repo.exists_by_id.assert_called_once_with(self.user_id)
        self.product_repo.exists_by_id.assert_called_once_with(self.item.product_id)
        self.cart_repo.get_cart_by_user_id.assert_not_called()
        self.cart_repo.save.assert_not_called()

    async def test_execute_item_already_exists_raises(self):
        # Given
        self.cart.add_item(self.item)

        self.user_repo.exists_by_id.return_value = True
        self.product_repo.exists_by_id.return_value = True
        self.cart_repo.get_cart_by_user_id.return_value = self.cart

        # When, Then
        with self.assertRaises(RecordAlreadyExistsError) as context:
            await self.use_case.execute(self.user_id, self.item)

        self.user_repo.exists_by_id.assert_called_once_with(self.user_id)
        self.product_repo.exists_by_id.assert_called_once_with(self.item.product_id)
        self.cart_repo.get_cart_by_user_id.assert_called_once_with(self.user_id)
        self.cart_repo.save.assert_not_called()

        self.assertEqual(
            f'Product with id={self.item.product_id} already exists in cart with id={self.cart.id}',
            str(context.exception)
        )
