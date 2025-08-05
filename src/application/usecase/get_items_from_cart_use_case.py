from typing import List

from src.application.error import RecordNotFoundError
from src.application.repository import CartRepository
from src.application.repository import ProductImageRepository
from src.application.repository import ProductRepository
from src.application.repository import UserRepository
from src.application.shared.result.cart_item_data import CartItemData
from src.application.usecase.mapper import to_cart_item_data_list


class GetItemsFromCartUseCase:
    
    def __init__(self, cart_repo: CartRepository, user_repo: UserRepository, product_repo: ProductRepository, product_image_repo: ProductImageRepository):
        self.cart_repo = cart_repo
        self.user_repo = user_repo
        self.product_repo = product_repo
        self.product_image_repo = product_image_repo

    async def execute(self, user_id: int) -> List[CartItemData]:
        if not await self.user_repo.exists_by_id(user_id):
            raise RecordNotFoundError.user_by_id(user_id)

        cart_items = await self.cart_repo.get_items_by_user_id(user_id)
        products_ids = [item.product_id for item in cart_items]

        products = await self.product_repo.get_all_by_ids(products_ids)
        image_urls = await self.product_image_repo.get_image_urls_by_product_ids(products_ids)

        return to_cart_item_data_list(cart_items, products, image_urls)