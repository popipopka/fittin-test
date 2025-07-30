from typing import List, Dict

from src.core.model import Category
from src.core.port.input import GetCategoriesPort
from src.core.port.output.category_repository import CategoryRepository
from src.core.shared.result import CategoryData


class GetCategoriesUseCase(GetCategoriesPort):

    def __init__(self, category_repo: CategoryRepository):
        self.category_repo = category_repo

    def execute(self) -> List[CategoryData]:
        categories = self.category_repo.get_all()

        return self.__build_category_tree(categories)

    @staticmethod
    def __build_category_tree(categories: List[Category]) -> List[CategoryData]:
        id_to_category_data: Dict[int, CategoryData] = {}

        for category in categories:
            id_to_category_data[category.id] = CategoryData.from_model(category)

        category_tree: List[CategoryData] = []
        for category in categories:
            category_data = id_to_category_data[category.id]

            if category.parent_id is None:
                category_tree.append(category_data)
            else:
                parent = id_to_category_data[category.parent_id]
                parent.children.add(category_data)

        return category_tree