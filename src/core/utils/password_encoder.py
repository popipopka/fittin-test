from abc import ABC, abstractmethod


class PasswordEncoder(ABC):
    @abstractmethod
    def encode(self, password: str) -> str:
        pass

    @abstractmethod
    def is_matched(self, value: str, encoded: str) -> bool:
        pass