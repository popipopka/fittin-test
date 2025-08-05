from decimal import Decimal

from parameterized import parameterized

from src.application.shared.enum import SortDirection
from src.application.shared.params import ProductFilterParams
from src.infrastructure.database.entity import ProductEntity, CategoryEntity
from src.infrastructure.database.repository import SqlProductRepository
from tests.infrastructure.database.repository.async_postgres_test_case import AsyncPostgresTestCase


class TestSqlProductRepository(AsyncPostgresTestCase):

    async def asyncSetUp(self):
        await super().asyncSetUp()
        await self.fill_data_in_database()

        self.repo = SqlProductRepository(self.session)

    async def fill_data_in_database(self):
        products = [
            ProductEntity(category_id=1,
                          name=f'name{i}',
                          description=f'desc{i}',
                          price=i)
            for i in range(1, 4)
        ]

        category = CategoryEntity(name='category')

        self.session.add(category)
        self.session.add_all(products)

        await self.session.commit()

    async def test_exist_by_id_return_true(self):
        # Given
        # When
        actual = await self.repo.exists_by_id(1)

        # Then
        self.assertTrue(actual)

    async def test_exist_by_id_return_false(self):
        # Given
        # When
        actual = await self.repo.exists_by_id(999)

        # Then
        self.assertFalse(actual)

    async def test_get_by_id_product_exists(self):
        # Given
        # When
        actual = await self.repo.get_by_id(1)
        # Then
        self.assertIsNotNone(actual)
        self.assertEqual(1, actual.id)

    async def test_get_by_id_product_not_exists(self):
        # When
        actual = await self.repo.get_by_id(999)

        # Then
        self.assertIsNone(actual)

    @parameterized.expand([
        ('empty_category',
         2,
         ProductFilterParams(),
         []
         ),
        ('not_empty_category',
         1,
         ProductFilterParams(),
         [1, 2, 3]
         ),
        ('no_filters',
         1,
         ProductFilterParams(),
         [1, 2, 3]
         ),
        ('min_price_filter',
         1,
         ProductFilterParams(min_price=Decimal('2')),
         [2, 3]
         ),
        ('max_price_filter',
         1,
         ProductFilterParams(max_price=Decimal('2')),
         [1, 2]
         ),
        ('price_between',
         1,
         ProductFilterParams(min_price=Decimal('2'), max_price=Decimal('2')),
         [2]
         ),
        ('sort_price_asc',
         1,
         ProductFilterParams(price_sort_direction=SortDirection.ASC),
         [1, 2, 3],
         True
         ),
        ('sort_price_desc',
         1,
         ProductFilterParams(price_sort_direction=SortDirection.DESC),
         [3, 2, 1],
         True
         )
    ])
    async def test_get_all_by_category_id(self, test_label, category_id: int, filters, expected_ids,
                                          is_strict_equal: bool = False):
        # Given
        # When
        result = await self.repo.get_all_by_category_id(category_id=category_id, filters=filters)

        # Then
        if is_strict_equal:
            self.assertListEqual(expected_ids, [product.id for product in result])
        else:
            self.assertTrue(all(p.id in expected_ids for p in result))

    @parameterized.expand([
        ('empty', []),
        ('not_empty', [1, 3]),
    ])
    async def test_get_all_by_ids(self, test_label, ids):
        # Given
        # When
        result = await self.repo.get_all_by_ids(ids)

        # Then
        self.assertTrue(all(p.id in ids for p in result))
