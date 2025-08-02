from src.adapter.input_port_fast_api.dto.request import RegisterRequest, LoginRequest
from src.adapter.input_port_fast_api.dto.response.tokens_response import TokensResponse
from src.core.shared.params import RegisterParams, LoginParams
from src.core.shared.result import TokensData


def to_register_params(register_request: RegisterRequest) -> RegisterParams:
    return RegisterParams(
        email=register_request.email,
        password=register_request.password,
    )

def to_login_params(login_request: LoginRequest) -> LoginParams:
    return LoginParams(
        email=login_request.email,
        password=login_request.password,
    )

def to_tokens_response(tokens_data: TokensData) -> TokensResponse:
    return TokensResponse(
        access_token=tokens_data.access_token,
        refresh_token=tokens_data.refresh_token,
    )