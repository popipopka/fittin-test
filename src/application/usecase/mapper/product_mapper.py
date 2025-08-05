from typing import List, Dict

from src.application.model import Product
from src.application.shared.result import ProductItemData


def to_product_item_data_list(products: List[Product], image_urls: Dict[int, str]) -> List[ProductItemData]:
    return [ProductItemData(id=product.id,
                            name=product.name,
                            price=product.price,
                            image_url=image_urls[product.id])
            for product in products]