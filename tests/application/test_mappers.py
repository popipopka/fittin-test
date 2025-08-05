import unittest
from decimal import Decimal

from parameterized import parameterized

from src.application.model import Product
from src.application.model.value import CartItem, OrderItem
from src.application.shared.result import CartItemData
from src.application.shared.result.product_item_data import ProductItemData
from src.application.usecase.mapper import to_product_item_data_list, to_cart_item_data_list, to_order_item_list


class TestMappers(unittest.TestCase):

    @parameterized.expand([
        ('empty', [], [], []),

        ('only',
         [Product(1, 1, 'name1', 'desc1', Decimal('1'))],
         {1: 'url1'},
         [ProductItemData(1, 'name1', Decimal('1'), 'url1')]
         ),

        ('many',
         [
             Product(1, 1, 'name1', 'desc1', Decimal('1')),
             Product(2, 2, 'name2', 'desc2', Decimal('2')),
             Product(3, 3, 'name3', 'desc3', Decimal('3')),
             Product(4, 4, 'name4', 'desc4', Decimal('4')),
         ],
         {1: 'url1', 2: 'url2', 3: 'url3', 4: 'url4'},
         [
             ProductItemData(1, 'name1', Decimal('1'), 'url1'),
             ProductItemData(2, 'name2', Decimal('2'), 'url2'),
             ProductItemData(3, 'name3', Decimal('3'), 'url3'),
             ProductItemData(4, 'name4', Decimal('4'), 'url4'),
         ]
         ),
    ])
    def test_to_product_item_data_list(self, test_label, products, image_urls, expected):
        # Given
        # When
        actual = to_product_item_data_list(products=products, image_urls=image_urls)

        # Then
        self.assertEqual(expected, actual)

    @parameterized.expand([
        ('empty', [], [], [], []),

        ('only',
         [CartItem(1, 1)],
         [Product(1, 1, 'name1', 'desc1', Decimal('1'))],
         {1: 'url1'},
         [CartItemData(ProductItemData(1, 'name1', Decimal('1'), 'url1'), 1)]
         ),

        ('many',
         [
             CartItem(1, 1),
             CartItem(2, 2),
             CartItem(3, 3),
             CartItem(4, 4),
         ],
         [
             Product(1, 1, 'name1', 'desc1', Decimal('1')),
             Product(2, 2, 'name2', 'desc2', Decimal('2')),
             Product(3, 3, 'name3', 'desc3', Decimal('3')),
             Product(4, 4, 'name4', 'desc4', Decimal('4')),
         ],
         {1: 'url1', 2: 'url2', 3: 'url3', 4: 'url4'},
         [
             CartItemData(ProductItemData(1, 'name1', Decimal('1'), 'url1'), 1),
             CartItemData(ProductItemData(2, 'name2', Decimal('2'), 'url2'), 2),
             CartItemData(ProductItemData(3, 'name3', Decimal('3'), 'url3'), 3),
             CartItemData(ProductItemData(4, 'name4', Decimal('4'), 'url4'), 4),
         ]
         ),
    ])
    def test_to_cart_item_data_list(self, test_label, cart_items, products, image_urls, expected):
        # Given
        # When
        actual = to_cart_item_data_list(cart_items=cart_items, products=products, image_urls=image_urls)

        # Then
        self.assertEqual(expected, actual)

    @parameterized.expand([
        ('empty', [], [], []),

        ('only',
         [CartItem(1, 1)],
         [Product(1, 1, 'name1', 'desc1', Decimal('1'))],
         [OrderItem(1, Decimal('1'), 1)]
         ),

        ('many',
         [
             CartItem(1, 1),
             CartItem(2, 2),
             CartItem(3, 3),
             CartItem(4, 4),
         ],
         [
             Product(1, 1, 'name1', 'desc1', Decimal('1')),
             Product(2, 2, 'name2', 'desc2', Decimal('2')),
             Product(3, 3, 'name3', 'desc3', Decimal('3')),
             Product(4, 4, 'name4', 'desc4', Decimal('4')),
         ],
         [
             OrderItem(1, Decimal('1'), 1),
             OrderItem(2, Decimal('2'), 2),
             OrderItem(3, Decimal('3'), 3),
             OrderItem(4, Decimal('4'), 4),
         ]
         ),
    ])
    def test_to_order_item_list(self, test_label, cart_items, products, expected):
        # Given
        # When
        actual = to_order_item_list(cart_items=cart_items, products=products)

        # Then
        self.assertEqual(expected, actual)