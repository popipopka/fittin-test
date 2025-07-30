from dataclasses import dataclass

from .product_item_data import ProductItemData


@dataclass
class CartItemData:
    product: ProductItemData
    quantity: int