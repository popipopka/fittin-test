import atexit
import io
from typing import Optional
from unittest import IsolatedAsyncioTestCase

from minio import Minio
from testcontainers.minio import MinioContainer

from src.adapter.output_port_minio import MinioProductImageRepository
from src.config import app_config


class MinioContainerManager:
    container = None
    client: Optional[Minio] = None

    @classmethod
    def start(cls):
        if cls.container:
            return

        cls.container = MinioContainer(image='minio/minio:latest')
        cls.container.start()

        cls.client = cls.container.get_client()

        bucket_name = app_config.object_storage.product_images_bucket
        if not cls.client.bucket_exists(bucket_name):
            cls.client.make_bucket(bucket_name)

    @classmethod
    def stop(cls):
        if cls.container:
            cls.container.stop()

            cls.container = None
            cls.client = None


atexit.register(MinioContainerManager.stop)


class TestMinioProductImageRepository(IsolatedAsyncioTestCase):

    @classmethod
    def setUpClass(cls):
        MinioContainerManager.start()

        cls.minio_client = MinioContainerManager.client
        cls.bucket_name = app_config.object_storage.product_images_bucket

    async def asyncSetUp(self):
        img_data = b'image data'
        for i in range(1, 4):
            self.minio_client.put_object(
                bucket_name=self.bucket_name,
                object_name=str(i),
                data=io.BytesIO(img_data),
                length=len(img_data),
                content_type="image/png"
            )

        self.repo = MinioProductImageRepository(self.minio_client)

    async def test_get_image_urls_by_product_ids(self):
        # Given
        product_ids = [1, 3]

        # When
        urls = await self.repo.get_image_urls_by_product_ids(product_ids)

        # Then
        self.assertSetEqual(set(urls.keys()), set(product_ids))
        self.assertTrue(all(url.startswith('http://') for url in urls.values()))

    async def test_get_image_url_by_product_id(self):
        # Given
        product_id = 2

        # When
        url = await self.repo.get_image_url_by_product_id(product_id)

        # Then
        self.assertTrue(url.startswith('http://'))