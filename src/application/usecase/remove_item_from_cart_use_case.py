from src.core.error import RecordNotFoundError
from src.core.port.input import RemoveItemFromCartPort
from src.core.port.output.cart_repository import CartRepository
from src.core.port.output.user_repository import UserRepository


class RemoveItemFromCartUseCase(RemoveItemFromCartPort):

    def __init__(self, cart_repository: CartRepository, user_repo: UserRepository):
        self.cart_repository = cart_repository
        self.user_repo = user_repo

    async def execute(self, user_id: int, product_id: int) -> None:
        if not await self.user_repo.exists_by_id(user_id):
            raise RecordNotFoundError.user_by_id(user_id)

        cart = await self.cart_repository.get_cart_by_user_id(user_id)
        cart.remove_item_by_product_id(product_id)

        await self.cart_repository.save(cart)