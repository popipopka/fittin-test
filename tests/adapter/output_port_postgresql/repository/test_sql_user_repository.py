from src.adapter.output_port_postgresql.entity import UserEntity
from src.adapter.output_port_postgresql.repository import SqlUserRepository
from tests.adapter.output_port_postgresql.repository.async_postgres_test_case import AsyncPostgresTestCase


class TestSqlUserRepository(AsyncPostgresTestCase):

    async def asyncSetUp(self):
        await super().asyncSetUp()

        self.repo = SqlUserRepository(self.session)

    async def test_exists_by_id_user_exists(self):
        # Given
        user = UserEntity(id=1, email='john@doe.com', hash_password="{hash}")
        self.session.add(user)
        await self.session.commit()

        # When
        actual = await self.repo.exists_by_id(user.id)

        # Then
        self.assertTrue(actual)

    async def test_exists_by_id_user_not_exists(self):
        # Given
        # When
        actual = await self.repo.exists_by_id(999)

        # Then
        self.assertFalse(actual)
