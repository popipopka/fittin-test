import os
import unittest
from datetime import timedelta
from unittest.mock import patch

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

        self.assertEqual('localhost:9900', config.object_storage.endpoint)
        self.assertEqual('local', config.object_storage.access_key)
        self.assertEqual('password', config.object_storage.secret_key)
        self.assertFalse(config.object_storage.secure)
        self.assertEqual('images', config.object_storage.product_images_bucket)
        self.assertEqual(timedelta(days=1), config.object_storage.product_image_url_expiration)

        self.assertEqual(
            '6zHqP7d/fRa9L9miftHVdPhyn0TtvlfRO2wB6LxjwALMvbNDQ7i34nlCYrOhPWDUBknos8yjaGHbj3U5m0baMw==',
            config.jwt.access_secret
        )
        self.assertEqual(
            'dDvsW+n6KAzZHLpeZ7c9bJavXt16MqRcEKFpmFytVxovNfDgzzCLOLT4RBVEXhXZT58TNshQWQTWeXrD5+rupw==',
            config.jwt.refresh_secret
        )
        self.assertEqual(timedelta(days=1), config.jwt.access_expiration)
        self.assertEqual(timedelta(days=30), config.jwt.refresh_expiration)

        self.assertEqual('localhost', config.smtp.server)
        self.assertEqual(1025, config.smtp.port)
        self.assertEqual('', config.smtp.username)
        self.assertEqual('', config.smtp.password)
        self.assertEqual('fittin@test.ru', config.smtp.email)

    @patch.dict(os.environ,
                {
                    'DEBUG': 'true',
                    'DATABASE__USER': 'user',
                    'OBJECT_STORAGE__ENDPOINT': 'endpoint',
                    'JWT__ACCESS_SECRET': 'access_secret',
                    'SMTP__SERVER': 'server',
                },
                clear=False
                )
    def test_local_config_from_env(self):
        # Given
        # When
        config = LocalConfig()

        # Then
        self.assertTrue(config.debug)
        self.assertEqual('user', config.database.user)
        self.assertEqual('password', config.database.password)
        self.assertEqual('localhost', config.database.host)
        self.assertEqual(5450, config.database.port)
        self.assertEqual('store', config.database.database)
        self.assertEqual('postgresql', config.database.dialect)

        self.assertEqual('endpoint', config.object_storage.endpoint)
        self.assertEqual('local', config.object_storage.access_key)
        self.assertEqual('password', config.object_storage.secret_key)
        self.assertFalse(config.object_storage.secure)
        self.assertEqual('images', config.object_storage.product_images_bucket)
        self.assertEqual(timedelta(days=1), config.object_storage.product_image_url_expiration)

        self.assertEqual('access_secret', config.jwt.access_secret)
        self.assertEqual(
            'dDvsW+n6KAzZHLpeZ7c9bJavXt16MqRcEKFpmFytVxovNfDgzzCLOLT4RBVEXhXZT58TNshQWQTWeXrD5+rupw==',
            config.jwt.refresh_secret
        )
        self.assertEqual(timedelta(days=1), config.jwt.access_expiration)
        self.assertEqual(timedelta(days=30), config.jwt.refresh_expiration)

        self.assertEqual('server', config.smtp.server)
        self.assertEqual(1025, config.smtp.port)
        self.assertEqual('', config.smtp.username)
        self.assertEqual('', config.smtp.password)
        self.assertEqual('fittin@test.ru', config.smtp.email)
