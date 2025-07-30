import os
import sys
import unittest
from unittest.mock import patch


class TestConfig(unittest.TestCase):
    def setUp(self):
        if "src.config" in sys.modules:
            del sys.modules["src.config"]

    def test_config_import_default_profile(self):
        # Given
        from src.config.local_config import LocalConfig
        expected = LocalConfig()

        # When
        import src.config as config
        actual = config.config

        # Then
        self.assertEqual(expected, actual)

    @patch.dict(os.environ,
                {'PROFILE': 'local'},
                clear=True)
    def test_config_import_local_profile(self):
        # Given
        from src.config.local_config import LocalConfig
        expected = LocalConfig()

        # When
        import src.config as config
        actual = config.config

        # Then
        self.assertEqual(expected, actual)

    @patch.dict(os.environ,
                {'PROFILE': 'unknown'},
                clear=True)
    def test_config_import_unknown_profile(self):
        # Given
        # When, Then
        with self.assertRaises(ValueError) as context:
            import src.config as config
            _ = config.config

        self.assertEqual('Unknown profile: unknown', str(context.exception))
