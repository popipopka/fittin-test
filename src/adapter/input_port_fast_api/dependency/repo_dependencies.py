from fastapi.params import Depends

from src.adapter.output_port_minio import MinioProductImageRepository, minio_client
from src.adapter.output_port_postgresql import get_database_session
from src.adapter.output_port_postgresql.repository import SqlCartRepository, SqlCategoryRepository, SqlOrderRepository, \
    SqlProductRepository, SqlUserRepository
from src.core.port.output.cart_repository import CartRepository
from src.core.port.output.category_repository import CategoryRepository
from src.core.port.output.order_repository import OrderRepository
from src.core.port.output.product_image_repository import ProductImageRepository
from src.core.port.output.product_repository import ProductRepository
from src.core.port.output.user_repository import UserRepository


def get_cart_repository(session: Depends(get_database_session)) -> CartRepository:
    return SqlCartRepository(session)


def get_category_repository(session: Depends(get_database_session)) -> CategoryRepository:
    return SqlCategoryRepository(session)


def get_order_repository(session: Depends(get_database_session)) -> OrderRepository:
    return SqlOrderRepository(session)


def get_product_image_repository() -> ProductImageRepository:
    return MinioProductImageRepository(minio_client)


def get_product_repository(session: Depends(get_database_session)) -> ProductRepository:
    return SqlProductRepository(session)


def get_user_repository(session: Depends(get_database_session)) -> UserRepository:
    return SqlUserRepository(session)
