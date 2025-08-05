from typing import List, Sequence, Optional

from src.application.model import Product
from src.application.model.value import Attribute
from src.infrastructure.database.entity import ProductAttributesAssociation
from src.infrastructure.database.entity import ProductEntity


def to_product_model_list(product_entities: Sequence[ProductEntity]) -> List[Product]:
    return list(map(to_product_model, product_entities))


def to_product_model(product_entity: Optional[ProductEntity]) -> Optional[Product]:
    if not product_entity:
        return None

    return Product(
        id=product_entity.id,
        category_id=product_entity.category_id,
        name=product_entity.name,
        description=product_entity.description,
        price=product_entity.price,
        created_at=product_entity.created_at,
        attributes=__to_attribute_model_list(product_entity.attributes)
    )


def __to_attribute_model_list(product_attributes: Sequence[ProductAttributesAssociation]) -> List[Attribute]:
    return list(map(__to_attribute_model, product_attributes))


def __to_attribute_model(product_attribute: ProductAttributesAssociation) -> Attribute:
    return Attribute(
        name=product_attribute.attribute.name,
        value=product_attribute.value,
    )
