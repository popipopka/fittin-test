from src.application.error import RecordNotFoundError
from src.application.repository import CartRepository, UserRepository


class RemoveItemFromCartUseCase:

    def __init__(self, cart_repo: CartRepository, user_repo: UserRepository):
        self.cart_repo = cart_repo
        self.user_repo = user_repo

    async def execute(self, user_id: int, product_id: int) -> None:
        if not await self.user_repo.exists_by_id(user_id):
            raise RecordNotFoundError.user_by_id(user_id)

        cart = await self.cart_repo.get_cart_by_user_id(user_id)
        cart.remove_item_by_product_id(product_id)

        await self.cart_repo.save(cart)