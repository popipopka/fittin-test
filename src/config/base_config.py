from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseConfig(BaseModel):
    user: str = ''
    password: str = ''
    host: str = ''
    port: int = 0
    database: str = ''


class BaseConfig(BaseSettings):
    debug: bool = False
    database: DatabaseConfig = DatabaseConfig()

    model_config = SettingsConfigDict(
        env_file='.env',
        env_nested_delimiter='__',
        case_sensitive=False,
    )