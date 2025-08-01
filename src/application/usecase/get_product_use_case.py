from src.core.error import RecordNotFoundError
from src.core.model import Product
from src.core.port.input import GetProductPort
from src.core.port.output.product_image_repository import ProductImageRepository
from src.core.port.output.product_repository import ProductRepository


class GetProductUseCase(GetProductPort):

    def __init__(self, product_repo: ProductRepository, product_image_repo: ProductImageRepository):
        self.product_repo = product_repo
        self.product_image_repo = product_image_repo

    async def execute(self, product_id: int) -> Product:
        product = await self.product_repo.get_by_id(product_id)

        if not product:
            raise RecordNotFoundError.product(product_id)

        product.image_url = await self.product_image_repo.get_image_url_by_product_id(product_id)

        return product
