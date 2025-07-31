from abc import ABC, abstractmethod

from src.core.model import Order


class OrderRepository(ABC):
    @abstractmethod
    async def save(self, order: Order) -> int:
        pass