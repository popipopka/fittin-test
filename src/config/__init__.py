from .base_config import BaseConfig
from .config_loader import load_config

app_config: BaseConfig = load_config()

__all__ = ['app_config']