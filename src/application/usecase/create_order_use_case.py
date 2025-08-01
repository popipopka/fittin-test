from src.application import to_order_item_list
from src.core.error import RecordNotFoundError
from src.core.model import Order
from src.core.port.input import CreateOrderPort
from src.core.port.output.cart_repository import CartRepository
from src.core.port.output.order_repository import OrderRepository
from src.core.port.output.product_repository import ProductRepository
from src.core.port.output.user_repository import UserRepository


class CreateOrderUseCase(CreateOrderPort):

    def __init__(self,
                 order_repo: OrderRepository,
                 user_repo: UserRepository,
                 cart_repo: CartRepository,
                 product_repo: ProductRepository):
        self.order_repo = order_repo
        self.user_repo = user_repo
        self.cart_repo = cart_repo
        self.product_repo = product_repo

    async def execute(self, user_id: int) -> int:
        if not await self.user_repo.exists_by_id(user_id):
            raise RecordNotFoundError.user_by_id(user_id)

        cart = await self.cart_repo.get_cart_by_user_id(user_id)
        products = await self.product_repo.get_all_by_ids([item.product_id for item in cart.items])
        order_items = to_order_item_list(cart.items, products)

        new_order = Order(user_id=user_id).add_items(order_items)

        cart.empty()
        await self.cart_repo.save(cart)

        return await self.order_repo.save(new_order)
