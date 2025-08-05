from src.application.utils import JwtProvider, PasswordEncoder


def get_jwt_provider() -> JwtProvider:
    return JwtProvider()

def get_password_encoder() -> PasswordEncoder:
    return PasswordEncoder()