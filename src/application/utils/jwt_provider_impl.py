from datetime import datetime, timezone

from jose import jwt, JWTError

from src.config import app_config
from src.core.utils import JwtProvider

ACCESS_SECRET = app_config.jwt.access_secret
REFRESH_SECRET = app_config.jwt.refresh_secret

ACCESS_EXPIRATION = app_config.jwt.access_expiration
REFRESH_EXPIRATION = app_config.jwt.refresh_expiration

ALGORITHM = 'HS256'


class JwtProviderImpl(JwtProvider):

    def create_refresh_token(self, user_id: int) -> str:
        claims = {
            'sub': str(user_id),
            'exp': datetime.now(timezone.utc) + REFRESH_EXPIRATION,
            'iat': datetime.now(timezone.utc)
        }
        return jwt.encode(claims=claims, key=REFRESH_SECRET, algorithm=ALGORITHM)

    def create_access_token(self, user_id: int) -> str:
        claims = {
            'sub': str(user_id),
            'exp': datetime.now(timezone.utc) + ACCESS_EXPIRATION,
            'iat': datetime.now(timezone.utc)
        }
        return jwt.encode(claims=claims, key=ACCESS_SECRET, algorithm=ALGORITHM)

    def is_refresh_token_valid(self, refresh_token: str) -> bool:
        try:
            jwt.decode(refresh_token, key=REFRESH_SECRET, algorithms=[ALGORITHM])
            return True
        except JWTError:
            return False

    def is_access_token_valid(self, access_token: str) -> bool:
        try:
            jwt.decode(access_token, key=ACCESS_SECRET, algorithms=[ALGORITHM])
            return True
        except JWTError:
            return False

    def get_sub_from_access_token(self, access_token: str) -> int:
        payload = jwt.decode(access_token, key=ACCESS_SECRET, algorithms=[ALGORITHM])
        return int(payload['sub'])

    def get_sub_from_refresh_token(self, refresh_token: str) -> int:
        payload = jwt.decode(refresh_token, key=REFRESH_SECRET, algorithms=[ALGORITHM])
        return int(payload['sub'])

    def get_exp_from_refresh_token(self, refresh_token: str) -> datetime:
        payload = jwt.decode(refresh_token, key=REFRESH_SECRET, algorithms=[ALGORITHM])
        return datetime.fromtimestamp(payload['exp'])
