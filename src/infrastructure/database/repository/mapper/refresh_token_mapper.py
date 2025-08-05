from typing import Optional

from src.application.model.refresh_token import RefreshToken
from src.infrastructure.database.entity import RefreshTokenEntity


def to_refresh_token_entity(refresh_token_model: RefreshToken) -> RefreshTokenEntity:
    entity = RefreshTokenEntity(
        user_id=refresh_token_model.user_id,
        expires_at=refresh_token_model.expires_at,
        value=refresh_token_model.value,
    )
    if refresh_token_model.id:
        entity.id = refresh_token_model.id

    return entity


def to_refresh_token_model(refresh_token_entity: Optional[RefreshTokenEntity]) -> Optional[RefreshToken]:
    if not refresh_token_entity:
        return None

    return RefreshToken(
        user_id=refresh_token_entity.user_id,
        expires_at=refresh_token_entity.expires_at,
        value=refresh_token_entity.value,
        id=refresh_token_entity.id,
    )
