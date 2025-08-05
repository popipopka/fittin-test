from pydantic import BaseModel, Field


class IssueAccessTokenRequest(BaseModel):
    refresh_token: str = Field(description='Jwt токен обновления', example='lOihR0lzOTUlC3tyZBZyhJornDHCjKC8=')
