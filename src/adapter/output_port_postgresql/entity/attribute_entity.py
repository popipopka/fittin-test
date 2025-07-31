from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from .base import Base


class AttributeEntity(Base):
    __tablename__ = 'attributes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False, unique=True)