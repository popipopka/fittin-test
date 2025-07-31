from .base_config import BaseConfig, DatabaseConfig


class LocalConfig(BaseConfig):
    debug: bool = True

    database: DatabaseConfig = DatabaseConfig(
        user='local',
        password='password',
        host='localhost',
        port=5450,
        database='store',
        dialect='postgresql',
    )
