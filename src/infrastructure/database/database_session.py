from typing import Any, AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from src.config import app_config

DATABASE_URL = f'{app_config.database.build_url('asyncpg')}'

engine = create_async_engine(url=DATABASE_URL, echo=app_config.debug)

AsyncSessionFactory = async_sessionmaker(engine, expire_on_commit=False)


async def get_database_session() -> AsyncGenerator[AsyncSession, Any]:
    async with AsyncSessionFactory() as session:
        async with session.begin():
            yield session
