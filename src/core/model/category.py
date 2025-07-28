from dataclasses import dataclass
from typing import Optional


@dataclass(eq=False)
class Category:
    id: int
    name: str
    parent_id: Optional[int] = None

    def __eq__(self, other):
        if not isinstance(other, Category):
            return False
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
