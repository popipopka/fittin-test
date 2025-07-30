import importlib
import os

from .base_config import BaseConfig


def load_config() -> BaseConfig:
    profile = os.getenv('PROFILE', 'local')

    try:
        return __load_config_class(profile)

    except (ModuleNotFoundError, AttributeError) as ex:
        raise ValueError(f"Unknown profile: {profile}") from ex


def __load_config_class(profile: str) -> BaseConfig:
    module_name = f'src.config.{profile}_config'
    class_name = f'{profile.capitalize()}Config'

    module = importlib.import_module(module_name)

    return getattr(module, class_name)()
