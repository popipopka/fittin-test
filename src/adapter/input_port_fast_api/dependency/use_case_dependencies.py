from fastapi.params import Depends

from src.adapter.input_port_fast_api.dependency import get_cart_repository, get_user_repository, get_product_repository, \
    get_product_image_repository
from src.application.usecase.add_item_to_cart_use_case import AddItemToCartUseCase
from src.application.usecase.create_order_use_case import CreateOrderUseCase
from src.application.usecase.get_categories_use_case import GetCategoriesUseCase
from src.application.usecase.get_items_from_cart_use_case import GetItemsFromCartUseCase
from src.application.usecase.get_product_use_case import GetProductUseCase
from src.application.usecase.get_products_use_case import GetProductsUseCase
from src.application.usecase.remove_item_from_cart_use_case import RemoveItemFromCartUseCase
from src.application.usecase.update_item_in_cart_use_case import UpdateItemInCartUseCase
from src.core.port.input import GetCategoriesPort, CreateOrderPort, GetItemsFromCartPort, GetProductPort, \
    GetProductsPort, RemoveItemFromCartPort, UpdateItemInCartPort
from src.core.port.input.add_item_to_cart_port import AddItemToCartPort
from src.core.port.output.cart_repository import CartRepository
from src.core.port.output.category_repository import CategoryRepository
from src.core.port.output.order_repository import OrderRepository
from src.core.port.output.product_image_repository import ProductImageRepository
from src.core.port.output.product_repository import ProductRepository
from src.core.port.output.user_repository import UserRepository


def get_add_item_to_cart_port(
        cart_repo: CartRepository = Depends(get_cart_repository),
        user_repo: UserRepository = Depends(get_user_repository)
) -> AddItemToCartPort:
    return AddItemToCartUseCase(
        cart_repo=cart_repo,
        user_repo=user_repo
    )


def get_create_order_port(
        order_repo: OrderRepository = Depends(),
        user_repo: UserRepository = Depends(get_user_repository),
        cart_repo: CartRepository = Depends(get_cart_repository),
        product_repo: ProductRepository = Depends(get_product_repository)
) -> CreateOrderPort:
    return CreateOrderUseCase(
        order_repo=order_repo,
        user_repo=user_repo,
        cart_repo=cart_repo,
        product_repo=product_repo,
    )


def get_categories_port(
        category_repo: CategoryRepository = Depends()
) -> GetCategoriesPort:
    return GetCategoriesUseCase(
        category_repo=category_repo,
    )


def get_get_items_from_cart_port(
        cart_repo: CartRepository = Depends(get_cart_repository),
        user_repo: UserRepository = Depends(get_user_repository),
        product_repo: ProductRepository = Depends(get_product_repository),
        product_image_repo: ProductImageRepository = Depends(get_product_image_repository)
) -> GetItemsFromCartPort:
    return GetItemsFromCartUseCase(
        cart_repo=cart_repo,
        user_repo=user_repo,
        product_repo=product_repo,
        product_image_repo=product_image_repo
    )


def get_get_product_port(
        product_repo: ProductRepository = Depends(get_product_repository),
        product_image_repo: ProductImageRepository = Depends(get_product_image_repository)
) -> GetProductPort:
    return GetProductUseCase(
        product_repo=product_repo,
        product_image_repo=product_image_repo
    )


def get_get_products_port(
        product_repo: ProductRepository = Depends(get_product_repository),
        product_image_repo: ProductImageRepository = Depends(get_product_image_repository)
) -> GetProductsPort:
    return GetProductsUseCase(
        product_repo=product_repo,
        product_image_repo=product_image_repo
    )


def get_remove_item_from_cart_port(
        cart_repo: CartRepository = Depends(get_cart_repository),
        user_repo: UserRepository = Depends(get_user_repository)
) -> RemoveItemFromCartPort:
    return RemoveItemFromCartUseCase(
        cart_repository=cart_repo,
        user_repo=user_repo,
    )


def get_update_item_in_cart_port(
        cart_repo: CartRepository = Depends(get_cart_repository),
        user_repo: UserRepository = Depends(get_user_repository)
) -> UpdateItemInCartPort:
    return UpdateItemInCartUseCase(
        cart_repository=cart_repo,
        user_repo=user_repo,
    )
