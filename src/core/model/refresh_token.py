from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class RefreshToken:
    user_id: int
    value: str = field(repr=False)
    expires_at: datetime
    id: Optional[int] = None

    def __eq__(self, other):
        if not isinstance(other, RefreshToken):
            return False
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
