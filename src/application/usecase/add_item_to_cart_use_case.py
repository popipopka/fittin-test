from src.core.error import RecordNotFoundError
from src.core.model.value import CartItem
from src.core.port.input import AddItemToCartPort
from src.core.port.output import ProductRepository
from src.core.port.output.cart_repository import CartRepository
from src.core.port.output.user_repository import UserRepository


class AddItemToCartUseCase(AddItemToCartPort):

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