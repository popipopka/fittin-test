import atexit
from unittest.async_case import IsolatedAsyncioTestCase

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from testcontainers.postgres import PostgresContainer

from src.infrastructure.database.entity import Base


class PostgresContainerManager:
    postgres = None
    db_url = None

    @classmethod
    def start(cls):
        if cls.postgres is None:
            cls.postgres = PostgresContainer('postgres:17')
            cls.postgres.start()

            cls.db_url = cls.postgres.get_connection_url().replace("psycopg2", "asyncpg")

    @classmethod
    def stop(cls):
        if cls.postgres is not None:
            cls.postgres.stop()

            cls.postgres = None
            cls.db_url = None


atexit.register(PostgresContainerManager.stop)


class AsyncPostgresTestCase(IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls):
        PostgresContainerManager.start()
        cls.db_url = PostgresContainerManager.db_url

    async def asyncSetUp(self):
        self.engine = create_async_engine(self.db_url)

        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        self.AsyncSessionFactory = async_sessionmaker(self.engine, expire_on_commit=False)
        self.session = self.AsyncSessionFactory()

    async def asyncTearDown(self):
        await self.session.rollback()
        await self.session.close()

        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)

        await self.engine.dispose()
