from dataclasses import dataclass, field

from sortedcontainers import SortedList

from src.application.model import Category


@dataclass
class CategoryData:
    id: int
    name: str

    children: SortedList['CategoryData'] = field(default_factory=lambda: SortedList())

    @staticmethod
    def from_model(category: Category) -> 'CategoryData':
        return CategoryData(id=category.id, name=category.name)

    def __repr__(self):
        return f"CategoryData(id={self.id}, name='{self.name}', children={list(self.children)})"

    def __lt__(self, other):
        if not isinstance(other, CategoryData):
            return NotImplemented
        return self.name < other.name
