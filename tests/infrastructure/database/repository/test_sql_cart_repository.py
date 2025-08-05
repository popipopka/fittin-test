from src.application.model import Cart
from src.application.model.value import CartItem
from src.infrastructure.database.entity import CategoryEntity, ProductEntity, UserEntity, CartEntity, \
    CartItemEntity
from src.infrastructure.database.repository import SqlCartRepository
from tests.infrastructure.database.repository.async_postgres_test_case import AsyncPostgresTestCase


class TestSqlCartRepository(AsyncPostgresTestCase):

    async def asyncSetUp(self):
        await super().asyncSetUp()
        await self.fill_data_in_database()

        self.repo = SqlCartRepository(self.session)

    async def fill_data_in_database(self):
        category = CategoryEntity(id=1, name='category')
        product = ProductEntity(id=1, category_id=1, name='name', description='desc', price=1)
        user = UserEntity(id=1, email='john@doe.con', hash_password='{hash}')

        self.session.add_all([category, product, user])
        await self.session.commit()

    async def test_get_items_by_user_id(self):
        # Given
        initial_cart = CartEntity(id=1, user_id=1)
        item = CartItemEntity(product_id=1, quantity=1)
        initial_cart.items = [item]

        self.session.add(initial_cart)
        await self.session.commit()

        # When
        actual_items = await self.repo.get_items_by_user_id(1)

        # Then
        actual_item = actual_items[0]

        self.assertEqual(len(actual_items), 1)
        self.assertEqual(item.product_id, actual_item.product_id)
        self.assertEqual(item.quantity, actual_item.quantity)

    async def test_get_cart_by_user_id_return_cart(self):
        # Given
        initial_cart = CartEntity(id=1, user_id=1)
        self.session.add(initial_cart)
        await self.session.commit()

        expected = Cart(id=1, user_id=1)

        # When
        actual = await self.repo.get_cart_by_user_id(1)

        # Then
        self.assertEqual(expected, actual)

    async def test_get_cart_by_user_id_return_none(self):
        # Given
        # When
        actual = await self.repo.get_cart_by_user_id(999)

        # Then
        self.assertIsNone(actual)

    async def test_save_creates_new_cart(self):
        # Given
        item = CartItem(product_id=1, quantity=1)

        cart = Cart(user_id=1)
        cart.add_item(item)

        # When
        cart_id = await self.repo.save(cart)

        # Then
        cart_from_db = await self.session.get(CartEntity, cart_id)
        item_from_db = cart_from_db.items[0]

        self.assertIsNotNone(cart_from_db)

        self.assertEqual(cart_from_db.id, item_from_db.cart_id)
        self.assertEqual(item.product_id, item_from_db.product_id)
        self.assertEqual(item.quantity, item_from_db.quantity)

    async def test_save_updates_existing_cart(self):
        # Given
        initial_cart = CartEntity(id=1, user_id=1)
        initial_cart.items = [CartItemEntity(product_id=1, quantity=1)]

        self.session.add(initial_cart)
        await self.session.commit()

        updated_cart_item = CartItem(product_id=1, quantity=2)
        updated_cart = Cart(id=1, user_id=1)
        updated_cart.add_item(updated_cart_item)

        # When
        cart_id = await self.repo.save(updated_cart)

        # Then
        cart_from_db = await self.session.get(CartEntity, cart_id)
        cart_item_from_db = cart_from_db.items[0]

        self.assertEqual(updated_cart.id, cart_from_db.id)
        self.assertEqual(updated_cart.user_id, cart_from_db.user_id)

        self.assertEqual(cart_id, cart_item_from_db.cart_id)
        self.assertEqual(updated_cart_item.product_id, cart_item_from_db.product_id)
        self.assertEqual(updated_cart_item.quantity, cart_item_from_db.quantity)
