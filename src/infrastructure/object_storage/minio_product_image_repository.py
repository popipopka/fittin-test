import asyncio
from typing import List, Dict

from minio import Minio

from src.application.repository import ProductImageRepository
from src.config import app_config


class MinioProductImageRepository(ProductImageRepository):
    __bucket_name = app_config.object_storage.product_images_bucket
    __expiration = app_config.object_storage.product_image_url_expiration

    def __init__(self, client: Minio):
        self.client = client

    async def get_image_urls_by_product_ids(self, product_ids: List[int]) -> Dict[int, str]:
        loop = asyncio.get_running_loop()

        return await loop.run_in_executor(
            None,
            self.__get_image_urls_sync,
            product_ids
        )

    async def get_image_url_by_product_id(self, product_id: int) -> str:
        loop = asyncio.get_running_loop()

        return await loop.run_in_executor(
            None,
            self.__get_image_url_sync,
            product_id
        )

    def __get_image_urls_sync(self, product_ids: List[int]) -> Dict[int, str]:
        images: Dict[int, str] = {}

        for product_id in product_ids:
            url = self.__get_image_url_sync(product_id)
            images[product_id] = url

        return images

    def __get_image_url_sync(self, product_id: int) -> str:
        return self.client.presigned_get_object(
            bucket_name=self.__bucket_name,
            object_name=str(product_id),
            expires=self.__expiration,
        )
