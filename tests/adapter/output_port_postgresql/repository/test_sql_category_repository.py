from src.adapter.output_port_postgresql.entity import CategoryEntity
from src.adapter.output_port_postgresql.repository import SqlCategoryRepository
from tests.adapter.output_port_postgresql.repository.async_postgres_test_case import AsyncPostgresTestCase


class TestSqlCategoryRepository(AsyncPostgresTestCase):

    async def asyncSetUp(self):
        await super().asyncSetUp()
        await self.fill_data_in_database()

        self.repo = SqlCategoryRepository(self.session)

    async def fill_data_in_database(self):
        category1 = CategoryEntity(id=1, name='category1')
        category2 = CategoryEntity(id=2, name='category2')
        category3 = CategoryEntity(id=3, name='category3')

        self.session.add_all([category1, category2, category3])
        await self.session.commit()

    async def test_get_all(self):
        # Given
        expected_ids = [1, 2, 3]

        # When
        categories = await self.repo.get_all()

        # Then
        self.assertTrue(all(c.id in expected_ids for c in categories))

    async def test_exists_category_exists(self):
        # Given
        # When
        actual = await self.repo.exists(1)

        # Then
        self.assertTrue(actual)

    async def test_exists_category_not_exists(self):
        # Given
        # When
        actual = await self.repo.exists(999)

        # Then
        self.assertFalse(actual)
