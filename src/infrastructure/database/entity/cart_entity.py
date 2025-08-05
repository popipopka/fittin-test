from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class CartEntity(Base):
    __tablename__ = 'carts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, unique=True)

    items = relationship(
        'CartItemEntity', back_populates='_cart', cascade='all, delete-orphan', lazy='joined'
    )
