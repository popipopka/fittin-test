from src.application.error import RecordAlreadyExistsError
from src.application.model import User, Cart
from src.application.repository import UserRepository, CartRepository
from src.application.shared.params.register_params import RegisterParams
from src.application.utils import PasswordEncoder


class RegisterUseCase:

    def __init__(self, user_repo: UserRepository, cart_repo: CartRepository, pass_encoder: PasswordEncoder):
        self.user_repo = user_repo
        self.cart_repo = cart_repo
        self.pass_encoder = pass_encoder

    async def execute(self, params: RegisterParams):
        email = params.email

        if await self.user_repo.exists_by_email(email):
            raise RecordAlreadyExistsError.user(email)

        new_user = User(
            email=email,
            hash_password=self.pass_encoder.encode(params.password),
        )
        new_user.id = await self.user_repo.save(new_user)

        new_cart = Cart(
            user_id=new_user.id,
        )
        await self.cart_repo.save(new_cart)