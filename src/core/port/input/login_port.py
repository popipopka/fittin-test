from abc import ABC, abstractmethod

from src.core.shared.params import LoginParams
from src.core.shared.result import TokensData


class LoginPort(ABC):
    @abstractmethod
    async def execute(self, params: LoginParams) -> TokensData:
        pass