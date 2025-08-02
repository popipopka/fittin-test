from sqlalchemy import Column, Integer, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship

from .base import Base


class CartItemEntity(Base):
    __tablename__ = 'cart_items'

    cart_id = Column(Integer, ForeignKey('carts.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)

    _cart = relationship('CartEntity', back_populates='items', lazy='raise')

    __table_args__ = (
        PrimaryKeyConstraint('cart_id', 'product_id'),
    )