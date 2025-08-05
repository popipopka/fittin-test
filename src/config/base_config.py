from datetime import timedelta

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseConfig(BaseModel):
    user: str = ''
    password: str = ''
    host: str = ''
    port: int = 0
    database: str = ''
    dialect: str = ''

    def build_url(self, driver: str) -> str:
        return f'{self.dialect}+{driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'


class ObjectStorageConfig(BaseModel):
    endpoint: str = ''
    access_key: str = ''
    secret_key: str = ''
    secure: bool = True

    product_images_bucket: str = 'images'
    product_image_url_expiration: timedelta = timedelta(days=1)


class JwtConfig(BaseModel):
    access_secret: str = ''
    refresh_secret: str = ''

    access_expiration: timedelta = timedelta(minutes=15)
    refresh_expiration: timedelta = timedelta(days=30)

class SmtpConfig(BaseModel):
    server: str = ''
    port: int = 0
    username: str = ''
    password: str = ''
    email: str = ''


class BaseConfig(BaseSettings):
    debug: bool = False

    database: DatabaseConfig = DatabaseConfig()
    object_storage: ObjectStorageConfig = ObjectStorageConfig()
    jwt: JwtConfig = JwtConfig()
    smtp: SmtpConfig = SmtpConfig()

    model_config = SettingsConfigDict(
        env_file='.env',
        env_nested_delimiter='__',
        case_sensitive=False,
    )
