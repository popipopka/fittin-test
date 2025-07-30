from .base_config import BaseConfig
from .config_loader import load_config

config: BaseConfig = load_config()

__all__ = ['config']