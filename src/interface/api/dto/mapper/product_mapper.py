from typing import List, Optional

from src.application.model import Product
from src.application.model.value import Attribute
from src.application.shared.params import ProductFilterParams
from src.application.shared.result import ProductItemData
from src.interface.api.dto.request import GetProductsRequest
from src.interface.api.dto.response import ProductResponse
from src.interface.api.dto.response.product_item_response import ProductItemResponse
from src.interface.api.dto.response.product_response import AttributeResponse


def to_product_response(product: Product) -> ProductResponse:
    return ProductResponse(
        id=product.id,
        category_id=product.category_id,
        name=product.name,
        description=product.description,
        price=product.price,
        image_url=product.image_url,
        attributes=__to_attribute_response_list(product.attributes),
    )


def __to_attribute_response_list(attributes: List[Attribute]) -> List[AttributeResponse]:
    return [AttributeResponse(
        name=attribute.name,
        value=attribute.value)
        for attribute in attributes]


def to_product_filter_params(get_products_request: Optional[GetProductsRequest]) -> Optional[ProductFilterParams]:
    if not get_products_request:
        return None

    return ProductFilterParams(
        min_price=get_products_request.min_price,
        max_price=get_products_request.max_price,
        price_sort_direction=get_products_request.price_sort_direction,
    )


def to_product_item_response_list(product_item_data_list: List[ProductItemData]) -> List[ProductItemResponse]:
    return list(map(to_product_item_response, product_item_data_list))


def to_product_item_response(product_item_data: ProductItemData) -> ProductItemResponse:
    return ProductItemResponse(
        id=product_item_data.id,
        name=product_item_data.name,
        price=product_item_data.price,
        image_url=product_item_data.image_url,
    )
