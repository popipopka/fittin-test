from sqlalchemy import Column, Integer, String, ForeignKey

from .base import Base


class CategoryEntity(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    parent_id = Column(Integer, ForeignKey('categories.id'), nullable=True, default=None)