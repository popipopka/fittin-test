from src.core.model import Product
from src.core.port.input import GetProductPort
from src.core.port.output.product_repository import ProductRepository


class GetProductUseCase(GetProductPort):

    def __init__(self, product_repo: ProductRepository):
        self.product_repo = product_repo

    async def execute(self, product_id: int) -> Product:
        return await self.product_repo.get_by_id(product_id)