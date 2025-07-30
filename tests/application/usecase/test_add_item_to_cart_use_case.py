import unittest
from unittest.mock import MagicMock

from src.application.usecase.add_item_to_cart_use_case import AddItemToCartUseCase
from src.core.error import RecordNotFoundError, RecordAlreadyExistsError
from src.core.model import Cart
from src.core.model.value import CartItem


class TestAddItemToCartUseCase(unittest.TestCase):
    def setUp(self):
        self.cart_repo = MagicMock()
        self.user_repo = MagicMock()

        self.use_case = AddItemToCartUseCase(self.cart_repo, self.user_repo)

        self.user_id = 1
        self.cart = Cart(1, self.user_id)
        self.item = CartItem(1, 1)

    def test_execute_success(self):
        # Given
        self.user_repo.exists_by_id.return_value = True
        self.cart_repo.get_cart_by_user_id.return_value = self.cart

        # When
        self.use_case.execute(self.user_id, self.item)

        # Then
        self.user_repo.exists_by_id.assert_called_once_with(self.user_id)
        self.cart_repo.get_cart_by_user_id.assert_called_once_with(self.user_id)
        self.cart_repo.save.assert_called_once()

    def test_execute_user_not_found_raises(self):
        # Given
        self.user_repo.exists_by_id.return_value = False

        # When, Then
        with self.assertRaises(RecordNotFoundError) as context:
            self.use_case.execute(self.user_id, self.item)

        self.assertEqual(f'User with id {self.user_id} not found', str(context.exception))

        self.user_repo.exists_by_id.assert_called_once_with(self.user_id)
        self.cart_repo.get_cart_by_user_id.assert_not_called()
        self.cart_repo.save.assert_not_called()


    def test_execute_item_already_exists_raises(self):
        # Given
        self.cart.add_item(self.item)

        self.user_repo.exists_by_id.return_value = True
        self.cart_repo.get_cart_by_user_id.return_value = self.cart

        # When, Then
        with self.assertRaises(RecordAlreadyExistsError) as context:
            self.use_case.execute(self.user_id, self.item)

        self.user_repo.exists_by_id.assert_called_once_with(self.user_id)
        self.cart_repo.get_cart_by_user_id.assert_called_once_with(self.user_id)
        self.cart_repo.save.assert_not_called()

        self.assertEqual(
            f'Product with id={self.item.product_id} already exists in cart with id={self.cart.id}',
            str(context.exception)
        )
