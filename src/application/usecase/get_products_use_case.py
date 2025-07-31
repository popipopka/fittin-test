from typing import Optional, List

from src.application.mappers import to_product_item_data_list
from src.core.port.input import GetProductsPort
from src.core.port.output.product_image_repository import ProductImageRepository
from src.core.port.output.product_repository import ProductRepository
from src.core.shared.params import ProductFilterParams
from src.core.shared.result.product_item_data import ProductItemData


class GetProductsUseCase(GetProductsPort):

    def __init__(self, product_repo: ProductRepository, product_image_repo: ProductImageRepository):
        self.product_repo = product_repo
        self.product_image_repo = product_image_repo

    async def execute(self, category_id: int, filters: Optional[ProductFilterParams] = None) -> List[ProductItemData]:
        if filters is None:
            filters = ProductFilterParams()

        products = await self.product_repo.get_all(filters)
        image_urls = await (self.product_image_repo
                            .get_image_urls_by_product_ids([product.id for product in products]))

        return to_product_item_data_list(products, image_urls)
