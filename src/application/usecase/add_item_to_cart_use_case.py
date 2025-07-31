from src.core.error import RecordNotFoundError
from src.core.model.value import CartItem
from src.core.port.input import AddItemToCartPort
from src.core.port.output.cart_repository import CartRepository
from src.core.port.output.user_repository import UserRepository


class AddItemToCartUseCase(AddItemToCartPort):

    def __init__(self, cart_repo: CartRepository, user_repo: UserRepository):
        self.cart_repo = cart_repo
        self.user_repo = user_repo

    async def execute(self, user_id: int, item: CartItem) -> None:
        if not await self.user_repo.exists_by_id(user_id):
            raise RecordNotFoundError.user(user_id)

        cart = await self.cart_repo.get_cart_by_user_id(user_id)
        cart.add_item(item)

        await self.cart_repo.save(cart)