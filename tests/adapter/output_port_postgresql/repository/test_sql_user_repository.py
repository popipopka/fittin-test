from src.adapter.output_port_postgresql.entity import UserEntity
from src.adapter.output_port_postgresql.repository import SqlUserRepository
from src.core.model import User
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

    async def test_exists_by_id_email_exists(self):
        # Given
        user = UserEntity(id=1, email='john@doe.com', hash_password="{hash}")
        self.session.add(user)
        await self.session.commit()

        # When
        actual = await self.repo.exists_by_email(user.email)

        # Then
        self.assertTrue(actual)

    async def test_exists_by_id_email_not_exists(self):
        # Given
        # When
        actual = await self.repo.exists_by_email('non@existing.email')

        # Then
        self.assertFalse(actual)

    async def test_save_creates_user(self):
        # Given
        user = User(email='john@doe.com', hash_password="{hash}")

        # When
        user_id = await self.repo.save(user)

        # Then
        entity_from_db = await self.session.get(UserEntity, user_id)

        self.assertIsNotNone(entity_from_db)
        self.assertEqual(user.email, entity_from_db.email)
        self.assertEqual(user.hash_password, entity_from_db.hash_password)
        self.assertEqual(user.created_at, entity_from_db.created_at)

    async def test_save_updates_existing_user(self):
        # Given
        initial_user = UserEntity(id=1, email='john@doe.com', hash_password="{hash}")
        self.session.add(initial_user)
        await self.session.commit()

        updated_user = User(id=1, email='new@user.email', hash_password="{new_hash}")

        # When
        user_id = await self.repo.save(updated_user)

        # Then
        entity_from_db = await self.session.get(UserEntity, user_id)

        self.assertEqual(updated_user.email, entity_from_db.email)
        self.assertEqual(updated_user.hash_password, entity_from_db.hash_password)
        self.assertEqual(updated_user.created_at, entity_from_db.created_at)

    async def test_get_by_email_return_user(self):
        # Given
        user = UserEntity(id=1, email='john@doe.com', hash_password="{hash}")
        self.session.add(user)
        await self.session.commit()

        expected = User(id=1, email='john@doe.com', hash_password="{hash}")

        # When
        actual = await self.repo.get_by_email(user.email)

        # Then
        self.assertEqual(expected, actual)

    async def test_get_by_email_return_none(self):
        # Given
        # When
        actual = await self.repo.get_by_email('unknown@user.email')

        # Then
        self.assertIsNone(actual)

    async def test_get_by_id_return_user(self):
        # Given
        user = UserEntity(id=1, email='john@doe.com', hash_password="{hash}")
        self.session.add(user)
        await self.session.commit()

        expected = User(id=1, email='john@doe.com', hash_password="{hash}")

        # When
        actual = await self.repo.get_by_id(user.id)

        # Then
        self.assertEqual(expected, actual)

    async def test_get_by_id_return_none(self):
        # Given
        # When
        actual = await self.repo.get_by_id(999)

        # Then
        self.assertIsNone(actual)