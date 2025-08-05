from sqlalchemy import Column, Integer, Numeric, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship

from .base import Base


class OrderItemEntity(Base):
    __tablename__ = 'order_items'

    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)

    unit_price = Column(Numeric(10, 3), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)

    _order = relationship('OrderEntity', back_populates='items', lazy='raise')

    __table_args__ = (
        PrimaryKeyConstraint('order_id', 'product_id'),
    )
