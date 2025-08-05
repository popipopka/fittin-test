from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from src.application.error import AuthenticationError
from src.application.utils import JwtProvider
from src.interface.dependency.utils_dependencies import get_jwt_provider

token_bearer_provider = HTTPBearer()


def get_authentication_principal(
        bearer_token: HTTPAuthorizationCredentials = Depends(token_bearer_provider),
        jwt_provider: JwtProvider = Depends(get_jwt_provider)
) -> int:
    access_token = bearer_token.credentials

    if not jwt_provider.is_access_token_valid(access_token):
        raise AuthenticationError.invalid_access_token()

    return jwt_provider.get_sub_from_access_token(access_token)
