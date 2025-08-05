from abc import ABC, abstractmethod
from typing import Optional

from src.application.model import User


class UserRepository(ABC):
    @abstractmethod
    async def exists_by_id(self, user_id: int) -> bool:
        pass

    @abstractmethod
    async def exists_by_email(self, email: str) -> bool:
        pass

    @abstractmethod
    async def save(self, user: User) -> int:
        pass

    @abstractmethod
    async def get_by_email(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    async def get_by_id(self, user_id: int) -> Optional[User]:
        pass