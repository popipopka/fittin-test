from datetime import timedelta

from .base_config import BaseConfig, DatabaseConfig, ObjectStorageConfig, JwtConfig


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
    jwt: JwtConfig = JwtConfig(
        access_secret='6zHqP7d/fRa9L9miftHVdPhyn0TtvlfRO2wB6LxjwALMvbNDQ7i34nlCYrOhPWDUBknos8yjaGHbj3U5m0baMw==',
        refresh_secret='dDvsW+n6KAzZHLpeZ7c9bJavXt16MqRcEKFpmFytVxovNfDgzzCLOLT4RBVEXhXZT58TNshQWQTWeXrD5+rupw==',
        access_expiration=timedelta(days=1),
        refresh_expiration=timedelta(days=30),
    )
