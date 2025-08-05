from src.application.error import RecordNotFoundError
from src.application.model import Order, User
from src.application.repository import CartRepository
from src.application.repository import NotificationSender
from src.application.repository import OrderRepository
from src.application.repository import ProductRepository
from src.application.repository import UserRepository
from src.application.usecase.mapper import to_order_item_list, to_order_created_notifications_params


class CreateOrderUseCase:

    def __init__(self,
                 order_repo: OrderRepository,
                 user_repo: UserRepository,
                 cart_repo: CartRepository,
                 product_repo: ProductRepository,
                 notification_sender: NotificationSender):
        self.order_repo = order_repo
        self.user_repo = user_repo
        self.cart_repo = cart_repo
        self.product_repo = product_repo
        self.notification_sender = notification_sender

    async def execute(self, user_id: int) -> int:
        user = await self.__get_user_by_id_or_throw(user_id)

        cart = await self.cart_repo.get_cart_by_user_id(user.id)
        if cart.is_empty():
            raise RecordNotFoundError.cart_items_in_cart(cart.id)

        products = await self.product_repo.get_all_by_ids([item.product_id for item in cart.items])
        order_items = to_order_item_list(cart.items, products)

        new_order = Order(user_id=user_id).add_items(order_items)
        new_order.id = await self.order_repo.save(new_order)

        cart.empty()
        await self.cart_repo.save(cart)

        await self.notification_sender.send_order_created(
            to_order_created_notifications_params(user_email=user.email, order=new_order, products=products)
        )

        return new_order.id

    async def __get_user_by_id_or_throw(self, user_id: int) -> User:
        user = await self.user_repo.get_by_id(user_id)

        if not user:
            raise RecordNotFoundError.user_by_id(user_id)

        return user
