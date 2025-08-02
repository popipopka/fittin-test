from aiosmtplib import SMTP
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.adapter.output_port_minio import MinioProductImageRepository, minio_client
from src.adapter.output_port_postgresql import get_database_session
from src.adapter.output_port_postgresql.repository import SqlCartRepository, SqlCategoryRepository, SqlOrderRepository, \
    SqlProductRepository, SqlUserRepository, SqlRefreshTokenRepository
from src.adapter.output_port_smtp.email_sender import EmailSender
from src.adapter.output_port_smtp.smtp_client import get_smtp_client
from src.core.port.output import RefreshTokenRepository, NotificationSender
from src.core.port.output.cart_repository import CartRepository
from src.core.port.output.category_repository import CategoryRepository
from src.core.port.output.order_repository import OrderRepository
from src.core.port.output.product_image_repository import ProductImageRepository
from src.core.port.output.product_repository import ProductRepository
from src.core.port.output.user_repository import UserRepository


def get_cart_repository(session: AsyncSession = Depends(get_database_session)) -> CartRepository:
    return SqlCartRepository(session)


def get_category_repository(session: AsyncSession = Depends(get_database_session)) -> CategoryRepository:
    return SqlCategoryRepository(session)


def get_order_repository(session: AsyncSession = Depends(get_database_session)) -> OrderRepository:
    return SqlOrderRepository(session)


def get_product_image_repository() -> ProductImageRepository:
    return MinioProductImageRepository(minio_client)


def get_product_repository(session: AsyncSession = Depends(get_database_session)) -> ProductRepository:
    return SqlProductRepository(session)


def get_user_repository(session: AsyncSession = Depends(get_database_session)) -> UserRepository:
    return SqlUserRepository(session)

def get_refresh_token_repository(session: AsyncSession = Depends(get_database_session)) -> RefreshTokenRepository:
    return SqlRefreshTokenRepository(session)

def get_notification_sender(smtp_client: SMTP = Depends(get_smtp_client)) -> NotificationSender:
    return EmailSender(client=smtp_client)