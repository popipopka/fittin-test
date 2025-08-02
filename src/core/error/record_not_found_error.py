class RecordNotFoundError(Exception):
    @staticmethod
    def cart_item(cart_id: int, product_id: int) -> 'RecordNotFoundError':
        return RecordNotFoundError(f'Product with id {product_id} not found in cart with id {cart_id}')

    @staticmethod
    def user_by_id(user_id: int) -> 'RecordNotFoundError':
        return RecordNotFoundError(f'User with id {user_id} not found')

    @staticmethod
    def user_by_email(email: str) -> 'RecordNotFoundError':
        return RecordNotFoundError(f'User with email {email} not found')

    @staticmethod
    def product(product_id: int) -> 'RecordNotFoundError':
        return RecordNotFoundError(f'Product with id {product_id} not found')

    @staticmethod
    def category(category_id: int) -> 'RecordNotFoundError':
        return RecordNotFoundError(f'Category with id {category_id} not found')

    @staticmethod
    def cart_items_in_cart(cart_id: int) -> 'RecordNotFoundError':
        return RecordNotFoundError(f'Cart items not found in cart with id={cart_id}')