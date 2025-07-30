import os
import unittest
from unittest.mock import patch

from src.config.base_config import BaseConfig


class TestBaseConfig(unittest.TestCase):
    @patch.dict(os.environ,
                {
                    'DEBUG': 'true',
                    'DATABASE__USER': 'user',
                    'DATABASE__PASSWORD': 'password',
                    'DATABASE__HOST': 'host',
                    'DATABASE__PORT': '1',
                    'DATABASE__DATABASE': 'database',
                },
                clear=False
                )
    def test_base_config_from_env(self):
        # Given
        # When
        config = BaseConfig()

        # Then
        self.assertTrue(config.debug)
        self.assertEqual('user', config.database.user)
        self.assertEqual('password', config.database.password)
        self.assertEqual('host', config.database.host)
        self.assertEqual(1, config.database.port)
        self.assertEqual('database', config.database.database)

    def test_base_config_default(self):
        # Given
        # When
        config = BaseConfig()

        # Then
        self.assertFalse(config.debug)
        self.assertEqual('', config.database.user)
        self.assertEqual('', config.database.password)
        self.assertEqual('', config.database.host)
        self.assertEqual(0, config.database.port)
        self.assertEqual('', config.database.database)
