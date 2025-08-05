from typing import Optional

from src.application.model import User
from src.infrastructure.database.entity import UserEntity


def to_user_entity(user_model: User) -> UserEntity:
    entity = UserEntity(
        hash_password=user_model.hash_password,
        created_at=user_model.created_at,
        email=user_model.email,
    )
    if user_model.id:
        entity.id = user_model.id

    return entity


def to_user_model(user_entity: UserEntity) -> Optional[User]:
    if not user_entity:
        return None

    return User(
        id=user_entity.id,
        email=user_entity.email,
        hash_password=user_entity.hash_password,
        created_at=user_entity.created_at,
    )
