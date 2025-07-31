from unittest.async_case import IsolatedAsyncioTestCase

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from testcontainers.postgres import PostgresContainer

from src.adapter.output_port_postgresql.entity import Base


class AsyncPostgresTestCase(IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls):
        cls.postgres = PostgresContainer('postgres:17')
        cls.postgres.start()

        cls.db_url = cls.postgres.get_connection_url().replace("psycopg2", "asyncpg")

    @classmethod
    def tearDownClass(cls):
        cls.postgres.stop()

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
