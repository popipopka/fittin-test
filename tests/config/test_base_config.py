import os
import unittest

from src.config.base_config import BaseConfig


class TestBaseConfig(unittest.TestCase):
    def test_base_config_from_env(self):
        # Given
        os.environ["DEBUG"] = "true"
        os.environ["DATABASE__USER"] = 'user'
        os.environ["DATABASE__PASSWORD"] = 'password'
        os.environ["DATABASE__HOST"] = 'host'
        os.environ["DATABASE__PORT"] = '1'
        os.environ["DATABASE__DATABASE"] = 'database'

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
