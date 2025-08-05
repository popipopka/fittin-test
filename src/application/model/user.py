from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional


@dataclass(eq=False)
class User:
    email: str
    hash_password: str = field(repr=False)
    id: Optional[int] = field(default=None)

    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)