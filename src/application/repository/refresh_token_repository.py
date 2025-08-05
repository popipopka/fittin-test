from abc import ABC, abstractmethod
from typing import Optional

from src.application.model.refresh_token import RefreshToken


class RefreshTokenRepository(ABC):
    @abstractmethod
    async def save(self, token: RefreshToken) -> int:
        pass

    @abstractmethod
    async def get_by_user_id(self, user_id: int) -> Optional[RefreshToken]:
        pass

    @abstractmethod
    async def exists_by_user_id(self, user_id: int) -> bool:
        pass