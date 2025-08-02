from datetime import timedelta

from pydantic import model_validator

from .base_config import BaseConfig, DatabaseConfig, ObjectStorageConfig, JwtConfig, SmtpConfig


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
    )
    smtp: SmtpConfig = SmtpConfig(
        server='localhost',
        username='',
        port=1025,
        password='',
    )

    @model_validator(mode='after')
    def merge_nested_configs(cls, values):
        for field_name in ['database', 'object_storage', 'jwt', 'smtp']:
            field = cls.model_fields[field_name]

            default_value = field.default
            if default_value is None:
                continue

            current_value = getattr(values, field_name, None)
            if current_value is None:
                setattr(values, field_name, default_value)
            else:
                merged = default_value.model_copy(update=current_value.model_dump(exclude_unset=True))
                setattr(values, field_name, merged)

        return values
