import os
import sys
import unittest


class TestConfig(unittest.TestCase):
    def setUp(self):
        if "src.config" in sys.modules:
            del sys.modules["src.config"]

    def test_config_import_default_profile(self):
        # Given
        if "PROFILE" in os.environ:
            del os.environ["PROFILE"]

        from src.config.local_config import LocalConfig
        expected_class_name = LocalConfig.__name__

        # When
        import src.config as config
        actual_class_name = config.config.__name__

        # Then
        self.assertEqual(actual_class_name, expected_class_name)

    def test_config_import_local_profile(self):
        # Given
        os.environ['PROFILE'] = 'local'

        from src.config.local_config import LocalConfig
        expected_class_name = LocalConfig.__name__

        # When
        import src.config as config
        actual_class_name = config.config.__name__

        # Then
        self.assertEqual(actual_class_name, expected_class_name)

    def test_config_import_unknown_profile(self):
        # Given
        profile = 'unknown'

        os.environ['PROFILE'] = profile

        # When, Then
        with self.assertRaises(ValueError) as context:
            import src.config as config
            _ = config.config

        self.assertEqual(f'Unknown profile: {profile}', str(context.exception))
