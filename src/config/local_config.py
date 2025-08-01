from .base_config import BaseConfig, DatabaseConfig, ObjectStorageConfig


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
    object_storage: ObjectStorageConfig = ObjectStorageConfig(
        endpoint='localhost:9900',
        access_key='local',
        secret_key='password',
        secure=False,
    )
