from fastapi import APIRouter, Depends

from src.application.usecase import RegisterUseCase, LoginUseCase, IssueAccessTokenUseCase
from src.interface.api.dto.mapper import to_register_params, to_login_params
from src.interface.api.dto.mapper.auth_mapper import to_tokens_response
from src.interface.api.dto.request import RegisterRequest, LoginRequest, IssueAccessTokenRequest
from src.interface.api.dto.response.tokens_response import TokensResponse
from src.interface.dependency import get_register_use_case, get_login_use_case, get_issue_access_token_use_case

router = APIRouter(
    prefix='/auth',
    tags=['Аутентификация'],
)


@router.post(
    '/register',
    summary='Регистрация пользователя',
    description='Регистрирует пользователя в системе и создает ему корзину',
    responses={
        200: {'description': 'Успешная регистрация', 'content': None},
        409: {'description': 'Пользователь уже существует'},
    }
)
async def register(
        body: RegisterRequest,
        port: RegisterUseCase = Depends(get_register_use_case)
) -> None:
    await port.execute(to_register_params(body))


@router.post(
    '/login',
    summary='Войти в систему',
    description='Входит в систему с помощью логина и пароля пользователя',
    responses={
        200: {'description': 'Успешный логин'},
        401: {'description': 'Ошибка аутентификации'},
    }
)
async def login(
        body: LoginRequest,
        port: LoginUseCase = Depends(get_login_use_case)
) -> TokensResponse:
    tokens = await port.execute(to_login_params(body))
    return to_tokens_response(tokens)


@router.post(
    '/token',
    summary='Обновить Jwt токена доступа',
    description='Обновляет Jwt токен доступа с помощью Jwt токена обновления',
    responses={
        200: {'description': 'Jwt токен доступа успешно обновлен'},
        401: {'description': 'Jwt токен обновления невалиден или отозван'},
    }
)
async def issue_access_token(
        body: IssueAccessTokenRequest,
        port: IssueAccessTokenUseCase = Depends(get_issue_access_token_use_case)
) -> str:
    return await port.execute(body.refresh_token)
