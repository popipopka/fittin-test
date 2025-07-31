from typing import List
from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock

from parameterized import parameterized
from sortedcontainers import SortedList

from src.application.usecase.get_categories_use_case import GetCategoriesUseCase
from src.core.model import Category
from src.core.shared.result import CategoryData


class TestGetCategoriesUseCase(IsolatedAsyncioTestCase):
    def setUp(self):
        self.category_repo = AsyncMock()
        self.use_case = GetCategoriesUseCase(self.category_repo)

    @parameterized.expand([
        ('empty', [], []),

        ('only_root',
         [Category(1, 'r1'), Category(2, 'r2'), Category(3, 'r3')],
         [CategoryData(1, 'r1'), CategoryData(2, 'r2'), CategoryData(3, 'r3')]),

        ('two_levels',
         [Category(1, 'r1'), Category(2, 'c1', 1), Category(3, 'c2', 1)],
         [
             CategoryData(1, 'r1', SortedList([
                 CategoryData(2, 'c1'),
                 CategoryData(3, 'c2'),
             ]))
         ]),

        ('multiple_levels',
         [
             Category(1, 'r1'), Category(2, 'r2'),
             Category(3, 'c1_r1', 1), Category(4, 'c1_r2', 2),
             Category(5, 'c1_c1_r1', 3), Category(6, 'c2_c1_r1', 3)
         ],
         [
             CategoryData(1, 'r1', SortedList([
                 CategoryData(3, 'c1_r1', SortedList([
                     CategoryData(5, 'c1_c1_r1'), CategoryData(6, 'c2_c1_r1'),
                 ])),
             ])),
             CategoryData(2, 'r2', SortedList([
                 CategoryData(4, 'c1_r2', SortedList([]))
             ]))
         ]
         )
    ])
    async def test_execute(self, test_label, categories: List[Category], expected_tree: List[CategoryData]):
        # Given
        self.category_repo.get_all.return_value = categories

        # When
        actual_tree = await self.use_case.execute()

        # Then
        self.assertEqual(expected_tree, actual_tree)

        self.category_repo.get_all.assert_called_once()
