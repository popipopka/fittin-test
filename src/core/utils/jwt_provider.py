from abc import ABC, abstractmethod
from datetime import datetime


class JwtProvider(ABC):
    @abstractmethod
    def create_refresh_token(self, user_id: int) -> str:
        pass

    @abstractmethod
    def create_access_token(self, user_id: int) -> str:
        pass

    @abstractmethod
    def is_refresh_token_valid(self, refresh_token: str) -> bool:
        pass

    @abstractmethod
    def is_access_token_valid(self, access_token: str) -> bool:
        pass

    @abstractmethod
    def get_sub_from_access_token(self, access_token: str) -> int:
        pass

    @abstractmethod
    def get_sub_from_refresh_token(self, refresh_token: str) -> int:
        pass

    @abstractmethod
    def get_exp_from_refresh_token(self, refresh_token: str) -> datetime:
        pass
