import unittest

from src.core.error import RecordAlreadyExistsError, RecordNotFoundError
from src.core.model import Cart
from src.core.model.value import CartItem


class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart(id=1, user_id=1)

        self.item1 = CartItem(1)
        self.item2 = CartItem(2)

    def test_is_empty_return_false(self):
        # Given
        self.cart.add_item(self.item1)

        # When
        actual = self.cart.is_empty()

        # Then
        self.assertFalse(actual)

    def test_is_empty_return_true(self):
        # Given
        # When
        actual = self.cart.is_empty()

        # Then
        self.assertTrue(actual)

    def test_add_item_success(self):
        # Given
        # When
        self.cart.add_item(self.item1)

        # Then
        self.assertIn(self.item1, self.cart.items)

    def test_add_item_already_exists_raises(self):
        # Given
        self.cart.add_item(self.item1)

        # When, Then
        with self.assertRaises(RecordAlreadyExistsError) as context:
            self.cart.add_item(self.item1)

        self.assertEqual(
            f'Product with id={self.item1.product_id} already exists in cart with id={self.cart.id}',
            str(context.exception)
        )

    def test_update_existing_item(self):
        # Given
        self.cart.add_item(CartItem(1))
        self.cart.add_item(CartItem(2))

        # When
        self.cart.update_item(CartItem(1, 2))

        # Then
        self.assertNotIn(CartItem(1), self.cart.items)
        self.assertIn(CartItem(1, 2), self.cart.items)
        self.assertIn(CartItem(2), self.cart.items)

    def test_update_nonexistent_item_not_found_raises(self):
        # Given
        item = CartItem(1)
        # When, Then
        with self.assertRaises(RecordNotFoundError) as context:
            self.cart.update_item(item)

        self.assertEqual(
            f'Product with id {item.product_id} not found in cart with id {self.cart.id}',
            str(context.exception)
        )

    def test_remove_existing_item_by_product_id_success(self):
        # Given
        self.cart.add_item(self.item1)
        self.cart.add_item(self.item2)

        # When
        self.cart.remove_item_by_product_id(self.item1.product_id)

        # Then
        self.assertNotIn(self.item1, self.cart.items)
        self.assertIn(self.item2, self.cart.items)

    def test_remove_nonexistent_item_by_product_id_item_not_found_raises(self):
        # Given
        self.cart.add_item(self.item2)

        # When
        with self.assertRaises(RecordNotFoundError) as context:
            self.cart.remove_item_by_product_id(self.item1.product_id)

        # Then
        self.assertIn(self.item2, self.cart.items)
        self.assertEqual(len(self.cart.items), 1)

        self.assertEqual(
            f'Product with id {self.item1.product_id} not found in cart with id {self.cart.id}',
            str(context.exception)
        )

    def test_empty(self):
        # Given
        self.cart.add_item(self.item1)
        self.cart.add_item(self.item2)

        # When
        self.cart.empty()

        # Then
        self.assertNotIn(self.item1, self.cart.items)
        self.assertNotIn(self.item2, self.cart.items)

    def test_equality(self):
        # Given
        first = Cart(id=1, user_id=2)
        second = Cart(id=1, user_id=4)

        # When, Then
        self.assertEqual(first, second)

    def test_inequality(self):
        # Given
        first = Cart(id=1, user_id=1)
        second = Cart(id=2, user_id=1)

        # When, Then
        self.assertNotEqual(first, second)
