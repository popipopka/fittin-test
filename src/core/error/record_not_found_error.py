class RecordNotFoundError(Exception):
    @staticmethod
    def cart_item(cart_id: int, product_id: int) -> 'RecordNotFoundError':
        return RecordNotFoundError(f'Product with id {product_id} not found in cart with id {cart_id}')

    @staticmethod
    def user(user_id: int) -> 'RecordNotFoundError':
        return RecordNotFoundError(f'User with id {user_id} not found')