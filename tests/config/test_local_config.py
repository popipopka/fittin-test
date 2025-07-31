import unittest

from src.config.local_config import LocalConfig


class TestLocalConfig(unittest.TestCase):
    def test_local_config(self):
        # Given
        # When
        config = LocalConfig()

        # Then
        self.assertTrue(config.debug)
        self.assertEqual('local', config.database.user)
        self.assertEqual('password', config.database.password)
        self.assertEqual('localhost', config.database.host)
        self.assertEqual(5450, config.database.port)
        self.assertEqual('store', config.database.database)
        self.assertEqual('postgresql', config.database.dialect)