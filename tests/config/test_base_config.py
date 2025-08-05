import os
import unittest
from unittest.mock import patch

from asyncpg.pgproto.pgproto import timedelta

from src.config.base_config import BaseConfig, DatabaseConfig


class TestBaseConfig(unittest.TestCase):
    @patch.dict(os.environ,
                {
                    'DEBUG': 'true',
                    'DATABASE__USER': 'user',
                    'DATABASE__PASSWORD': 'password',
                    'DATABASE__HOST': 'host',
                    'DATABASE__PORT': '1',
                    'DATABASE__DATABASE': 'database',

                    'OBJECT_STORAGE__ENDPOINT': 'endpoint',
                    'OBJECT_STORAGE__ACCESS_KEY': 'access_key',
                    'OBJECT_STORAGE__SECRET_KEY': 'secret_key',
                    'OBJECT_STORAGE__SECURE': 'false',
                    'OBJECT_STORAGE__PRODUCT_IMAGES_BUCKET': 'img_bucket',
                    'OBJECT_STORAGE__PRODUCT_IMAGE_URL_EXPIRATION': 'PT60M',

                    'JWT__ACCESS_SECRET': 'access_secret',
                    'JWT__REFRESH_SECRET': 'refresh_secret',
                    'JWT__ACCESS_EXPIRATION': 'PT60H',
                    'JWT__REFRESH_EXPIRATION': 'P60D',

                    'SMTP__SERVER': 'server',
                    'SMTP__PORT': '100',
                    'SMTP__USERNAME': 'username',
                    'SMTP__PASSWORD': 'password',
                    'SMTP__EMAIL': 'smtp@email.com',
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

        self.assertEqual('endpoint', config.object_storage.endpoint)
        self.assertEqual('access_key', config.object_storage.access_key)
        self.assertEqual('secret_key', config.object_storage.secret_key)
        self.assertFalse(config.object_storage.secure)
        self.assertEqual('img_bucket', config.object_storage.product_images_bucket)
        self.assertEqual(timedelta(minutes=60), config.object_storage.product_image_url_expiration)

        self.assertEqual('access_secret', config.jwt.access_secret)
        self.assertEqual('refresh_secret', config.jwt.refresh_secret)
        self.assertEqual(timedelta(hours=60), config.jwt.access_expiration)
        self.assertEqual(timedelta(days=60), config.jwt.refresh_expiration)

        self.assertEqual('server', config.smtp.server)
        self.assertEqual(100, config.smtp.port)
        self.assertEqual('username', config.smtp.username)
        self.assertEqual('password', config.smtp.password)
        self.assertEqual('smtp@email.com', config.smtp.email)

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

        self.assertEqual('', config.object_storage.endpoint)
        self.assertEqual('', config.object_storage.access_key)
        self.assertEqual('', config.object_storage.secret_key)
        self.assertTrue(config.object_storage.secure)
        self.assertEqual('images', config.object_storage.product_images_bucket)
        self.assertEqual(timedelta(days=1), config.object_storage.product_image_url_expiration)

        self.assertEqual('', config.jwt.access_secret)
        self.assertEqual('', config.jwt.refresh_secret)
        self.assertEqual(timedelta(minutes=15), config.jwt.access_expiration)
        self.assertEqual(timedelta(days=30), config.jwt.refresh_expiration)

        self.assertEqual('', config.smtp.server)
        self.assertEqual(0, config.smtp.port)
        self.assertEqual('', config.smtp.username)
        self.assertEqual('', config.smtp.password)
        self.assertEqual('', config.smtp.email)

    def test_database_config_build_url(self):
        # Given
        database_config = DatabaseConfig(
            user='user',
            password='pass',
            database='database',
            host='host',
            port=1111,
            dialect='dialect'
        )
        expected = 'dialect+driver://user:pass@host:1111/database'

        # When
        actual = database_config.build_url(driver='driver')

        # Then
        self.assertEqual(expected, actual)