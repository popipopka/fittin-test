from pydantic import BaseModel, Field


class TokensResponse(BaseModel):
    access_token: str = Field(description='Jwt токен доступа', examples=['dGhpc0lzQVRlc3RSZWZyZXNoVG9rZW4='])
    refresh_token: str = Field(description='Jwt токен обновления', examples=['lOihR0lzOTUlC3tyZBZyhJornDHCjKC8='])
