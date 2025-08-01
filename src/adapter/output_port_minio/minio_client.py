from minio import Minio

from src.config import app_config

minio_client = Minio(
    endpoint=app_config.object_storage.endpoint,
    access_key=app_config.object_storage.access_key,
    secret_key=app_config.object_storage.secret_key,
    secure=app_config.object_storage.secure,
)
