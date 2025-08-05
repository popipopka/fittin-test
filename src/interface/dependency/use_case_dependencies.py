from fastapi.params import Depends

from src.application.repository import CartRepository, RefreshTokenRepository, NotificationSender
from src.application.repository import CategoryRepository
from src.application.repository import OrderRepository
from src.application.repository import ProductImageRepository
from src.application.repository import ProductRepository
from src.application.repository import UserRepository
from src.application.usecase import AddItemToCartUseCase, LoginUseCase, IssueAccessTokenUseCase
from src.application.usecase import CreateOrderUseCase
from src.application.usecase import GetCategoriesUseCase
from src.application.usecase import GetItemsFromCartUseCase
from src.application.usecase import GetProductUseCase
from src.application.usecase import GetProductsUseCase
from src.application.usecase import RegisterUseCase
from src.application.usecase import RemoveItemFromCartUseCase
from src.application.usecase import UpdateItemInCartUseCase
from src.application.utils import PasswordEncoder, JwtProvider
from src.interface.dependency.repository_dependencies import get_cart_repository, \
    get_user_repository, \
    get_product_repository, \
    get_product_image_repository, get_category_repository, get_refresh_token_repository, get_order_repository, \
    get_notification_sender
from src.interface.dependency.utils_dependencies import get_password_encoder, get_jwt_provider


def get_add_item_to_cart_use_case(
        cart_repo: CartRepository = Depends(get_cart_repository),
        user_repo: UserRepository = Depends(get_user_repository),
        product_repo: ProductRepository = Depends(get_product_repository)
) -> AddItemToCartUseCase:
    return AddItemToCartUseCase(
        cart_repo=cart_repo,
        user_repo=user_repo,
        product_repo=product_repo
    )


def get_create_order_use_case(
        order_repo: OrderRepository = Depends(get_order_repository),
        user_repo: UserRepository = Depends(get_user_repository),
        cart_repo: CartRepository = Depends(get_cart_repository),
        product_repo: ProductRepository = Depends(get_product_repository),
        notification_sender: NotificationSender = Depends(get_notification_sender)
) -> CreateOrderUseCase:
    return CreateOrderUseCase(
        order_repo=order_repo,
        user_repo=user_repo,
        cart_repo=cart_repo,
        product_repo=product_repo,
        notification_sender=notification_sender
    )


def get_get_categories_use_case(
        category_repo: CategoryRepository = Depends(get_category_repository)
) -> GetCategoriesUseCase:
    return GetCategoriesUseCase(
        category_repo=category_repo,
    )


def get_get_items_from_cart_use_case(
        cart_repo: CartRepository = Depends(get_cart_repository),
        user_repo: UserRepository = Depends(get_user_repository),
        product_repo: ProductRepository = Depends(get_product_repository),
        product_image_repo: ProductImageRepository = Depends(get_product_image_repository)
) -> GetItemsFromCartUseCase:
    return GetItemsFromCartUseCase(
        cart_repo=cart_repo,
        user_repo=user_repo,
        product_repo=product_repo,
        product_image_repo=product_image_repo
    )


def get_get_product_use_case(
        product_repo: ProductRepository = Depends(get_product_repository),
        product_image_repo: ProductImageRepository = Depends(get_product_image_repository)
) -> GetProductUseCase:
    return GetProductUseCase(
        product_repo=product_repo,
        product_image_repo=product_image_repo
    )


def get_get_products_use_case(
        product_repo: ProductRepository = Depends(get_product_repository),
        product_image_repo: ProductImageRepository = Depends(get_product_image_repository),
        category_repo: CategoryRepository = Depends(get_category_repository),
) -> GetProductsUseCase:
    return GetProductsUseCase(
        product_repo=product_repo,
        product_image_repo=product_image_repo,
        category_repo=category_repo
    )


def get_remove_item_from_cart_use_case(
        cart_repo: CartRepository = Depends(get_cart_repository),
        user_repo: UserRepository = Depends(get_user_repository)
) -> RemoveItemFromCartUseCase:
    return RemoveItemFromCartUseCase(
        cart_repository=cart_repo,
        user_repo=user_repo,
    )


def get_update_item_in_cart_use_case(
        cart_repo: CartRepository = Depends(get_cart_repository),
        user_repo: UserRepository = Depends(get_user_repository)
) -> UpdateItemInCartUseCase:
    return UpdateItemInCartUseCase(
        cart_repository=cart_repo,
        user_repo=user_repo,
    )


def get_register_use_case(
        user_repo: UserRepository = Depends(get_user_repository),
        cart_repo: CartRepository = Depends(get_cart_repository),
        pass_encoder: PasswordEncoder = Depends(get_password_encoder)
) -> RegisterUseCase:
    return RegisterUseCase(
        user_repo=user_repo,
        cart_repo=cart_repo,
        pass_encoder=pass_encoder
    )


def get_login_use_case(
        user_repo: UserRepository = Depends(get_user_repository),
        pass_encoder: PasswordEncoder = Depends(get_password_encoder),
        jwt_provider: JwtProvider = Depends(get_jwt_provider),
        refresh_token_repo: RefreshTokenRepository = Depends(get_refresh_token_repository)
) -> LoginUseCase:
    return LoginUseCase(
        user_repo=user_repo,
        pass_encoder=pass_encoder,
        jwt_provider=jwt_provider,
        refresh_token_repo=refresh_token_repo
    )


def get_issue_access_token_use_case(
        jwt_provider: JwtProvider = Depends(get_jwt_provider),
        refresh_token_repo: RefreshTokenRepository = Depends(get_refresh_token_repository)
) -> IssueAccessTokenUseCase:
    return IssueAccessTokenUseCase(
        jwt_provider=jwt_provider,
        refresh_token_repo=refresh_token_repo
    )
