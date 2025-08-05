from abc import ABC, abstractmethod

from src.application.model import Order


class OrderRepository(ABC):
    @abstractmethod
    async def save(self, order: Order) -> int:
        pass