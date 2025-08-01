from datetime import datetime

from src.application.error import AuthenticationError
from src.core.port.input.issue_access_token_port import IssueAccessTokenPort
from src.core.port.output import RefreshTokenRepository
from src.core.utils import JwtProvider


class IssueAccessTokenUseCase(IssueAccessTokenPort):

    def __init__(self, jwt_provider: JwtProvider, refresh_token_repo: RefreshTokenRepository):
        self.jwt_provider = jwt_provider
        self.refresh_token_repo = refresh_token_repo

    async def execute(self, refresh_token: str) -> str:
        user_id = await self.__get_user_id_from_refresh_token(refresh_token)
        await self.__check_refresh_token_not_revoked(user_id)

        return self.jwt_provider.create_access_token(user_id)

    async def __get_user_id_from_refresh_token(self, refresh_token: str) -> int:
        if not self.jwt_provider.is_refresh_token_valid(refresh_token):
            raise AuthenticationError.invalid_refresh_token()

        return self.jwt_provider.get_sub_from_refresh_token(refresh_token)

    async def __check_refresh_token_not_revoked(self, user_id: int):
        saved = await self.refresh_token_repo.get_by_user_id(user_id)

        if not saved or datetime.now() >= saved.expires_at:
            raise AuthenticationError.revoked_refresh_token()
