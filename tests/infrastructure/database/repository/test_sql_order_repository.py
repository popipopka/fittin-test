from decimal import Decimal

from src.application.model import Order
from src.application.model.value import OrderItem
from src.infrastructure.database.entity import ProductEntity, CategoryEntity, OrderEntity, UserEntity, \
    OrderItemEntity
from src.infrastructure.database.repository import SqlOrderRepository
from tests.infrastructure.database.repository.async_postgres_test_case import AsyncPostgresTestCase


class TestSqlOrderRepository(AsyncPostgresTestCase):

    async def asyncSetUp(self):
        await super().asyncSetUp()
        await self.fill_data_in_database()

        self.repo = SqlOrderRepository(self.session)

    async def fill_data_in_database(self):
        category = CategoryEntity(id=1, name='category')
        product = ProductEntity(id=1, category_id=1, name='name', description='desc', price=1)
        user = UserEntity(id=1, email='john@doe.con', hash_password='{hash}')

        self.session.add_all([category, product, user])
        await self.session.commit()

    async def test_save_creates_new_order(self):
        # Given
        item = OrderItem(product_id=1, unit_price=Decimal('1'), quantity=1)

        order = Order(user_id=1).add_items([item])

        # When
        order_id = await self.repo.save(order)

        # Then
        entity_from_db = await self.session.get(OrderEntity, order_id)
        item_from_db = entity_from_db.items[0]

        self.assertIsNotNone(entity_from_db)

        self.assertEqual(order_id, item_from_db.order_id)
        self.assertEqual(item.product_id, item_from_db.product_id)
        self.assertEqual(item.unit_price, item_from_db.unit_price)
        self.assertEqual(item.quantity, item_from_db.quantity)

    async def test_save_updates_existing_order(self):
        # Given
        initial_order = OrderEntity(id=1, user_id=1)
        initial_order.items = [OrderItemEntity(product_id=1, unit_price=Decimal('1'), quantity=1)]

        self.session.add(initial_order)
        await self.session.commit()

        updated_order_item = OrderItem(product_id=1, unit_price=Decimal('1'), quantity=2)
        updated_order = (Order(id=1, user_id=1)
                         .add_items([updated_order_item]))

        # When
        updated_id = await self.repo.save(updated_order)

        # Then
        order_from_db = await self.session.get(OrderEntity, updated_id)
        order_item_from_db = order_from_db.items[0]

        self.assertEqual(updated_order.id, order_from_db.id)
        self.assertEqual(updated_order.user_id, order_from_db.user_id)

        self.assertEqual(updated_order_item.quantity, order_item_from_db.quantity)