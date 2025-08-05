from typing import Optional, List

from src.application.error import RecordNotFoundError
from src.application.repository import CategoryRepository
from src.application.repository import ProductImageRepository
from src.application.repository import ProductRepository
from src.application.shared.params import ProductFilterParams
from src.application.shared.result.product_item_data import ProductItemData
from src.application.usecase.mapper import to_product_item_data_list


class GetProductsUseCase:

    def __init__(self,
                 product_repo: ProductRepository,
                 product_image_repo: ProductImageRepository,
                 category_repo: CategoryRepository,
                 ):
        self.product_repo = product_repo
        self.product_image_repo = product_image_repo
        self.category_repo = category_repo

    async def execute(self, category_id: int, filters: Optional[ProductFilterParams] = None) -> List[ProductItemData]:
        if not await self.category_repo.exists(category_id):
            raise RecordNotFoundError.category(category_id)

        if filters is None:
            filters = ProductFilterParams()

        products = await self.product_repo.get_all_by_category_id(category_id, filters)
        image_urls = await (self.product_image_repo
                            .get_image_urls_by_product_ids([product.id for product in products]))

        return to_product_item_data_list(products, image_urls)
