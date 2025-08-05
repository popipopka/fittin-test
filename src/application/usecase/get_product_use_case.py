from src.application.error import RecordNotFoundError
from src.application.model import Product
from src.application.repository import ProductImageRepository
from src.application.repository import ProductRepository


class GetProductUseCase:

    def __init__(self, product_repo: ProductRepository, product_image_repo: ProductImageRepository):
        self.product_repo = product_repo
        self.product_image_repo = product_image_repo

    async def execute(self, product_id: int) -> Product:
        product = await self.product_repo.get_by_id(product_id)

        if not product:
            raise RecordNotFoundError.product(product_id)

        product.image_url = await self.product_image_repo.get_image_url_by_product_id(product_id)

        return product
