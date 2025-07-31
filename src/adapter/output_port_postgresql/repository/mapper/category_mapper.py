from typing import List, Sequence

from src.adapter.output_port_postgresql.entity import CategoryEntity
from src.core.model import Category


def to_category_model_list(category_entities: Sequence[CategoryEntity]) -> List[Category]:
    return  list(map(to_category_model, category_entities))

def to_category_model(category_entity: CategoryEntity) -> Category:
    return Category(
        id=category_entity.id,
        name=category_entity.name,
        parent_id=category_entity.parent_id,
    )