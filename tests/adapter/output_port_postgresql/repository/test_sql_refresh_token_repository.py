from datetime import datetime, timezone

from src.adapter.output_port_postgresql.entity import UserEntity, RefreshTokenEntity
from src.adapter.output_port_postgresql.repository import SqlRefreshTokenRepository
from src.core.model import RefreshToken
from tests.adapter.output_port_postgresql.repository.async_postgres_test_case import AsyncPostgresTestCase


class TestSqlRefreshTokenRepository(AsyncPostgresTestCase):

    async def asyncSetUp(self):
        await super().asyncSetUp()
        await self.fill_data_in_database()

        self.repo = SqlRefreshTokenRepository(self.session)

    async def fill_data_in_database(self):
        user = UserEntity(id=1, email='john@doe.con', hash_password='{hash}')

        self.session.add_all([user])
        await self.session.commit()

    async def test_save_creates_refresh_token(self):
        # Given
        refresh_token = RefreshToken(value='{value}', user_id=1, expires_at=datetime.now(timezone.utc))

        # When
        refresh_token_id = await self.repo.save(refresh_token)

        # Then
        entity_from_db = await self.session.get(RefreshTokenEntity, refresh_token_id)

        self.assertIsNotNone(entity_from_db)
        self.assertEqual(refresh_token.value, entity_from_db.value)
        self.assertEqual(refresh_token.user_id, entity_from_db.user_id)
        self.assertEqual(refresh_token.expires_at, entity_from_db.expires_at)

    async def test_save_updates_existing_refresh_token(self):
        # Given
        initial_refresh_token = RefreshTokenEntity(id=1, value='{value}', user_id=1, expires_at=datetime.now())
        self.session.add(initial_refresh_token)
        await self.session.commit()

        updated_refresh_token = RefreshToken(id=1, value='{new_value}', user_id=1,
                                             expires_at=datetime.now(timezone.utc))

        # When
        refresh_token_id = await self.repo.save(updated_refresh_token)

        # Then
        entity_from_db = await self.session.get(RefreshTokenEntity, refresh_token_id)

        self.assertEqual(updated_refresh_token.value, entity_from_db.value)
        self.assertEqual(updated_refresh_token.user_id, entity_from_db.user_id)
        self.assertEqual(updated_refresh_token.expires_at, entity_from_db.expires_at)

    async def test_get_by_user_id_return_refresh_token(self):
        # Given
        refresh_token = RefreshTokenEntity(id=1, value='{value}', user_id=1, expires_at=datetime.now())
        self.session.add(refresh_token)
        await self.session.commit()

        expected = RefreshToken(id=1, user_id=1, value='{value}', expires_at=datetime.now())

        # When
        actual = await self.repo.get_by_user_id(1)

        # Then
        self.assertEqual(actual, expected)

    async def test_get_by_user_id_return_none(self):
        # Given
        # When
        actual = await self.repo.get_by_user_id(999)

        # Then
        self.assertIsNone(actual)

    async def test_exists_by_user_id_return_true(self):
        # Given
        refresh_token = RefreshTokenEntity(id=1, value='{value}', user_id=1, expires_at=datetime.now())
        self.session.add(refresh_token)
        await self.session.commit()

        # When
        actual = await self.repo.exists_by_user_id(1)

        # Then
        self.assertTrue(actual)

    async def test_exists_by_user_id_return_false(self):
        # Given
        # When
        actual = await self.repo.exists_by_user_id(999)

        # Then
        self.assertFalse(actual)
