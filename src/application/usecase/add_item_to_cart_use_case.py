from src.application.error import RecordNotFoundError
from src.application.model.value import CartItem
from src.application.repository import CartRepository
from src.application.repository import ProductRepository
from src.application.repository import UserRepository


class AddItemToCartUseCase:

    def __init__(self, cart_repo: CartRepository, product_repo: ProductRepository, user_repo: UserRepository):
        self.cart_repo = cart_repo
        self.user_repo = user_repo
        self.product_repo = product_repo

    async def execute(self, user_id: int, new_item: CartItem) -> None:
        if not await self.user_repo.exists_by_id(user_id):
            raise RecordNotFoundError.user_by_id(user_id)

        if not await self.product_repo.exists_by_id(new_item.product_id):
            raise RecordNotFoundError.product(new_item.product_id)

        cart = await self.cart_repo.get_cart_by_user_id(user_id)
        cart.add_item(new_item)

        await self.cart_repo.save(cart)