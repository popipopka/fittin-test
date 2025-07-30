from abc import ABC, abstractmethod


class CreateOrderPort(ABC):
    @abstractmethod
    def execute(self, user_id: int):
        pass