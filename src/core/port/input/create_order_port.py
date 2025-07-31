from abc import ABC, abstractmethod


class CreateOrderPort(ABC):
    @abstractmethod
    async def execute(self, user_id: int) -> int:
        pass