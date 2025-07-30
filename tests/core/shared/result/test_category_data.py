import unittest

from parameterized import parameterized
from sortedcontainers import SortedList

from src.core.shared.result import CategoryData


class TestCategoryData(unittest.TestCase):
    @parameterized.expand([
        ('empty', [], []),
        ('only', [CategoryData(1, 'a')], [CategoryData(1, 'a')]),
        ('many',
         [CategoryData(1, 'e'), CategoryData(1, 'b'), CategoryData(1, 'a'), CategoryData(1, 'd'), CategoryData(1, 'c')],
         [CategoryData(1, 'a'), CategoryData(1, 'b'), CategoryData(1, 'c'), CategoryData(1, 'd'), CategoryData(1, 'e')]
         ),
    ])
    def test_children_sorting(self, test_label, init_children, expected_children):
        # Given
        # When
        actual_children = CategoryData(1, 'name', SortedList(init_children)).children

        # Then
        self.assertEqual(expected_children, actual_children)
