from .base_config import BaseConfig
from .config_loader import load_config

app_config: BaseConfig = load_config()

print(type(app_config))

print(app_config.database.database)
print(app_config.database.host)
print(app_config.database.dialect)
print(app_config.database.build_url("asyndfdsdf"))

__all__ = ['app_config']