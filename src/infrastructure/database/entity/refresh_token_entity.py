from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from src.infrastructure.database.entity import Base


class RefreshTokenEntity(Base):
    __tablename__ = 'refresh_tokens'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, unique=True)
    value = Column(String, nullable=False)
    expires_at = Column(DateTime(timezone=True), nullable=False)
