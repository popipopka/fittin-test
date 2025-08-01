from src.core.error import RecordAlreadyExistsError
from src.core.model import User, Cart
from src.core.port.input.register_port import RegisterPort
from src.core.port.output import UserRepository, CartRepository
from src.core.shared.params.register_params import RegisterParams
from src.core.utils import PasswordEncoder


class RegisterUseCase(RegisterPort):

    def __init__(self, user_repo: UserRepository, cart_repo: CartRepository, pass_encoder: PasswordEncoder):
        self.user_repo = user_repo
        self.cart_repo = cart_repo
        self.pass_encoder = pass_encoder

    def execute(self, params: RegisterParams):
        email = params.email

        if self.user_repo.exists_by_email(email):
            raise RecordAlreadyExistsError.user(email)

        new_user = User(
            email=email,
            hash_password=self.pass_encoder.encode(params.password),
        )
        new_cart = Cart(
            user_id=new_user.id,
        )

        self.user_repo.save(new_user)
        self.cart_repo.save(new_cart)