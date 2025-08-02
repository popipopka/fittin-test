from src.application.utils import BcryptPasswordEncoder, JwtProviderImpl
from src.core.utils import JwtProvider, PasswordEncoder


def get_jwt_provider() -> JwtProvider:
    return JwtProviderImpl()

def get_password_encoder() -> PasswordEncoder:
    return BcryptPasswordEncoder()