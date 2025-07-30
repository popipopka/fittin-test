import unittest
from decimal import Decimal
from unittest.mock import MagicMock

from src.application.usecase.create_order_use_case import CreateOrderUseCase
from src.core.error import RecordNotFoundError
from src.core.model import Product, Cart
from src.core.model.value import CartItem


class TestCreateOrderUseCase(unittest.TestCase):
    def setUp(self):
        self.order_repo = MagicMock()
        self.user_repo = MagicMock()
        self.cart_repo = MagicMock()
        self.product_repo = MagicMock()

        self.use_case = CreateOrderUseCase(self.order_repo, self.user_repo, self.cart_repo, self.product_repo)

        self.user_id = 1

    def test_execute_success(self):
        # Given

        cart = Cart(id=1, user_id=self.user_id)
        cart.add_item(CartItem(1, 1))
        cart.add_item(CartItem(2, 2))

        products = [
            Product(1, 1, 'name1', 'desc1', Decimal('1')),
            Product(2, 1, 'name2', 'desc2', Decimal('2')),
        ]

        self.user_repo.exists_by_id.return_value = True
        self.cart_repo.get_cart_by_user_id.return_value = cart
        self.product_repo.get_all_by_ids.return_value = products

        # When
        self.use_case.execute(self.user_id)

        # Then
        self.user_repo.exists_by_id.assert_called_once_with(self.user_id)
        self.cart_repo.get_cart_by_user_id.assert_called_once_with(self.user_id)
        self.product_repo.get_all_by_ids.assert_called_once_with([1, 2])
        self.order_repo.save.assert_called_once()
        self.cart_repo.save.assert_called_once()

    def test_execute_user_not_found_raises(self):
        # Given
        self.user_repo.exists_by_id.return_value = False

        # When, Then
        with self.assertRaises(RecordNotFoundError) as context:
            self.use_case.execute(self.user_id)

        self.assertEqual(f'User with id {self.user_id} not found', str(context.exception))

        self.user_repo.exists_by_id.assert_called_once_with(self.user_id)

        self.cart_repo.get_cart_by_user_id.assert_not_called()
        self.product_repo.get_all_by_ids.assert_not_called()
        self.order_repo.save.assert_not_called()
        self.cart_repo.save.assert_not_called()
