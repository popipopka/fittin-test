import unittest

from src.core.model import Category


class TestCategory(unittest.TestCase):
    def test_equality(self):
        # Given
        first = Category(1, 'name', 0)
        second = Category(1, 'name2', 2)

        # When, Then
        self.assertEqual(first, second)

    def test_inequality(self):
        # Given
        first = Category(1, 'name', 0)
        second = Category(2, 'name', 0)

        # When, Then
        self.assertNotEqual(first, second)