from abc import ABC, abstractmethod


class UserRepository(ABC):
    @abstractmethod
    async def exists_by_id(self, user_id: int) -> bool:
        pass