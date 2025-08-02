import unittest

from src.core.model import User


class TestUser(unittest.TestCase):
    def test_equality(self):
        # Given
        first = User(id=1, email='john@doe.com', hash_password='{hash}')
        second = User(id=1, email='john@doe.com', hash_password='{hash}')

        # When, Then
        self.assertEqual(first, second)

    def test_inequality(self):
        # Given
        first = User(id=1, email='john@doe.com', hash_password='{hash}')
        second = User(id=2, email='john@doe.com', hash_password='{hash}')

        # When, Then
        self.assertNotEqual(first, second)

    def test_hash_password_not_in_repr(self):
        # Given
        user = User(id=1, email="john@doe.com", hash_password="{hash}")

        # When
        repr_str = repr(user)

        # Then
        self.assertNotIn(f"hash_password='{user.hash_password}'", repr_str)
