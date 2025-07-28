from dataclasses import dataclass, field
from datetime import datetime


@dataclass(eq=False)
class User:
    id: int

    email: str
    hash_password: str = field(repr=False)

    created_at: datetime = field(default_factory=datetime.now)

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)