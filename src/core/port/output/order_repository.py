from abc import ABC, abstractmethod

from src.core.model import Order


class OrderRepository(ABC):
    @abstractmethod
    def save(self, order: Order):
        pass