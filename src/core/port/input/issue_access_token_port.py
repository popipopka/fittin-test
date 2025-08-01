from abc import ABC, abstractmethod


class IssueAccessTokenPort(ABC):
    @abstractmethod
    async def execute(self, refresh_token: str):
        pass