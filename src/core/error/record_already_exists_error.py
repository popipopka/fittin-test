class RecordAlreadyExistsError(Exception):
    @staticmethod
    def cart_item(cart_id: int, product_id: int) -> 'RecordAlreadyExistsError':
        return RecordAlreadyExistsError(f'Product with id={product_id} already exists in cart with id={cart_id}')

    @staticmethod
    def order_item(order_id: int, product_id: int) -> 'RecordAlreadyExistsError':
        return RecordAlreadyExistsError(f'Product with id={product_id} already exists in order with id={order_id}')

    @staticmethod
    def user(self, email: str) -> 'RecordAlreadyExistsError':
        return RecordAlreadyExistsError(f'User with email={email} already exists')