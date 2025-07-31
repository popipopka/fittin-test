from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class ProductAttributesAssociation(Base):
    __tablename__ = 'product_attributes'

    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    attribute_id = Column(Integer, ForeignKey('attributes.id'), primary_key=True)
    value = Column(String(64), nullable=False)

    _product = relationship('ProductEntity', back_populates='attributes', lazy='raise')
    attribute = relationship('AttributeEntity', lazy='joined')
