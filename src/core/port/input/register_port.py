from abc import ABC, abstractmethod

from src.core.shared.params.register_params import RegisterParams


class RegisterPort(ABC):
    @abstractmethod
    def execute(self, params: RegisterParams):
        pass