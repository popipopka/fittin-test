from src.application.error import AuthenticationError
from src.core.error import RecordNotFoundError
from src.core.model import User
from src.core.model.refresh_token import RefreshToken
from src.core.port.input.login_port import LoginPort
from src.core.port.output import RefreshTokenRepository, UserRepository
from src.core.shared.params import LoginParams
from src.core.shared.result import TokensData
from src.core.utils import PasswordEncoder, JwtProvider


class LoginUseCase(LoginPort):

    def __init__(self, user_repo: UserRepository, pass_encoder: PasswordEncoder, jwt_provider: JwtProvider,
                 refresh_token_repo: RefreshTokenRepository):
        self.user_repo = user_repo
        self.pass_encoder = pass_encoder
        self.jwt_provider = jwt_provider
        self.refresh_token_repo = refresh_token_repo

    async def execute(self, params: LoginParams) -> TokensData:
        user = await self.__get_user_or_raise(params.email)

        if not self.pass_encoder.is_matched(params.password, user.hash_password):
            raise AuthenticationError.wrong_password()

        access_token = self.jwt_provider.create_access_token(user.id)
        refresh_token = self.jwt_provider.create_refresh_token(user.id)

        await self.__update_or_save_refresh_token(user.id, refresh_token)

        return TokensData(
            access_token=access_token,
            refresh_token=refresh_token,
        )

    async def __get_user_or_raise(self, email: str) -> User:
        user = await self.user_repo.get_by_email(email)

        if not user:
            raise RecordNotFoundError.user_by_email(email)

        return user

    async def __update_or_save_refresh_token(self, user_id: int, plain_refresh_token: str):
        new_refresh_token = RefreshToken(
            user_id=user_id,
            value=plain_refresh_token,
            expires_at=self.jwt_provider.get_exp_from_refresh_token(plain_refresh_token)
        )

        saved_refresh_token = await self.refresh_token_repo.get_by_user_id(user_id)
        if saved_refresh_token:
            new_refresh_token.id = saved_refresh_token.id

        await self.refresh_token_repo.save(new_refresh_token)
