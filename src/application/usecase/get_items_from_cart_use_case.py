from typing import List

from src.application import to_cart_item_data_list
from src.core.error import RecordNotFoundError
from src.core.port.input import GetItemsFromCartPort
from src.core.port.output.cart_repository import CartRepository
from src.core.port.output.product_image_repository import ProductImageRepository
from src.core.port.output.product_repository import ProductRepository
from src.core.port.output.user_repository import UserRepository
from src.core.shared.params import ProductFilterParams
from src.core.shared.result.cart_item_data import CartItemData


class GetItemsFromCartUseCase(GetItemsFromCartPort):
    
    def __init__(self, cart_repo: CartRepository, user_repo: UserRepository, product_repo: ProductRepository, product_image_repo: ProductImageRepository):
        self.cart_repo = cart_repo
        self.user_repo = user_repo
        self.product_repo = product_repo
        self.product_image_repo = product_image_repo

    def execute(self, user_id: int) -> List[CartItemData]:
        if not self.user_repo.exists_by_id(user_id):
            raise RecordNotFoundError.user(user_id)

        cart_items = self.cart_repo.get_items_by_user_id(user_id)
        products_ids = [item.product_id for item in cart_items]

        products = self.product_repo.get_all_by_ids(products_ids)
        image_urls = self.product_image_repo.get_image_urls_by_product_ids(products_ids)

        return to_cart_item_data_list(cart_items, products, image_urls)