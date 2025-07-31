from typing import List, Sequence, Optional

from src.adapter.output_port_postgresql.entity import ProductAttributesAssociation
from src.adapter.output_port_postgresql.entity import ProductEntity
from src.core.model import Product
from src.core.model.value import Attribute


def to_product_model_list(product_entities: Sequence[ProductEntity]) -> List[Product]:
    return list(map(to_product_model, product_entities))


def to_product_model(product_entity: ProductEntity) -> Optional[Product]:
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
