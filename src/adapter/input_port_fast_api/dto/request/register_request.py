from pydantic import BaseModel, Field


class RegisterRequest(BaseModel):
    email: str = Field(description='Почта пользователя', min_length=1, max_length=255, examples=['email@example.com'])
    password: str = Field(description='Пароль пользователя', min_length=8, max_length=32, examples=['seCRetP@ss'])
