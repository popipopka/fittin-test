from fastapi import APIRouter, Depends

from src.adapter.input_port_fast_api.dependency import get_register_port, get_login_port, get_issue_access_token_port
from src.adapter.input_port_fast_api.dto.mapper import to_register_params, to_login_params
from src.adapter.input_port_fast_api.dto.mapper.auth_mapper import to_tokens_response
from src.adapter.input_port_fast_api.dto.request import RegisterRequest, LoginRequest, IssueAccessTokenRequest
from src.adapter.input_port_fast_api.dto.response.tokens_response import TokensResponse
from src.core.port.input import RegisterPort, LoginPort, IssueAccessTokenPort

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
        port: RegisterPort = Depends(get_register_port)
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
        port: LoginPort = Depends(get_login_port)
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
        port: IssueAccessTokenPort = Depends(get_issue_access_token_port)
) -> str:
    return await port.execute(body.refresh_token)
