from aiosmtplib import SMTP
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.repository import CartRepository
from src.application.repository import CategoryRepository
from src.application.repository import OrderRepository
from src.application.repository import ProductImageRepository
from src.application.repository import ProductRepository
from src.application.repository import RefreshTokenRepository, NotificationSender
from src.application.repository import UserRepository
from src.infrastructure.database import get_database_session
from src.infrastructure.database.repository import SqlCartRepository, SqlCategoryRepository, SqlOrderRepository, \
    SqlProductRepository, SqlUserRepository, SqlRefreshTokenRepository
from src.infrastructure.object_storage import MinioProductImageRepository, minio_client
from src.infrastructure.smtp.email_sender import EmailSender
from src.infrastructure.smtp.smtp_client import get_smtp_client


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