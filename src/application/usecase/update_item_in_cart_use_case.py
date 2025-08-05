from src.application.error import RecordNotFoundError
from src.application.model.value import CartItem
from src.application.repository import CartRepository
from src.application.repository import UserRepository


class UpdateItemInCartUseCase:

    def __init__(self, cart_repository: CartRepository, user_repo: UserRepository):
        self.cart_repository = cart_repository
        self.user_repo = user_repo

    async def execute(self, user_id: int, updated_item: CartItem) -> None:
        if not await self.user_repo.exists_by_id(user_id):
            raise RecordNotFoundError.user_by_id(user_id)

        cart = await self.cart_repository.get_cart_by_user_id(user_id)
        cart.update_item(updated_item)

        await self.cart_repository.save(cart)