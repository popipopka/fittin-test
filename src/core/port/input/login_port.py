from abc import ABC, abstractmethod

from src.core.shared.params import LoginParams


class LoginPort(ABC):
    @abstractmethod
    async def execute(self, params: LoginParams):
        pass